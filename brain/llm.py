import os # t access environment variables
from typing import Optional, Literal # optional means that the field can be None, Any means it can be any type, and Literal allows us to specify exact string values for the type field

from dotenv import load_dotenv
from google import genai
from google.genai import types # it provides the GenerateContentConfig class, which is used to configure how Gemini generates content like json responses
from pydantic import BaseModel # it helps us give the structured response we want from Gemini, and it also helps us validate that the response we get back is in the correct format like the particular json response we need 


# -----------------------------------
# 1. Load environment variables
# -----------------------------------

load_dotenv()


# -----------------------------------
# 2. Get Gemini API key
# -----------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# -----------------------------------
# 3. Create Gemini client
# -----------------------------------

client = genai.Client(api_key=API_KEY)


# -----------------------------------
# 4. Load Lyra's system prompt
# -----------------------------------

with open(
    "brain/prompts/lyra_brain.txt",
    "r",
    encoding="utf-8" #used for reading text files -->reads normal text and also special characters -->standard safe choice for reading text files 
) as file: # opens file as an easy name so basically file is lyra_brain.txt and we can use it to read the file
    SYSTEM_PROMPT = file.read()


# -----------------------------------
# 5. Define Lyra's response structure
# -----------------------------------
class LyraArguments(BaseModel): #possible arguments that can be passed to the tools that lyra can use
    application: Optional[str] = None
    project: Optional[str] = None
    folder: Optional[str] = None
    filename: Optional[str] = None
    query: Optional[str] = None
    site: Optional[str] = None


class LyraResponse(BaseModel):
    type: Literal["chat", "tool", "web"] #if chat then makes lyra speak and if its tool then executes a somputer action and if web makes the router do a web search 

    tool: Optional[str] = None #it can either be a string or none cuz if its open vs code or smtg thne it is a string but if its chat the it will be none 

    arguments: Optional[LyraArguments] = None # if it is a tool then it is a dictionary otherwise if its a chat then no need therefore it is null and it is any cuz different tools use different kinds or arguements 
    # this is an example of arguement "application": "Visual Studio Code"
    answer: Optional[str] = None # if it is chat then it is a string otherwise if its a tool then no need therefore it is null


# -----------------------------------
# 6. Ask Lyra's Brain
# -----------------------------------

def ask_llm(command: str) -> dict: # the function other python files will call when they want to ask lyra brain smtg 
# command parameter should be a string 
#-->dict is a type hint ...the function is expected to return a dictionary 
    try: # if somtg goes wrong in the following block instead of crashing go to except block

        response = client.models.generate_content( # actually sends request to Gemini
            model="gemini-3.8-flash",

            contents=command,#user input 

            config=types.GenerateContentConfig( #how gemini should respond to the request 

                # Lyra's instructions
                system_instruction=SYSTEM_PROMPT,

                # Force Gemini to return JSON
                response_mime_type="application/json",

                # Force JSON to follow LyraResponse
                response_schema=LyraResponse,
                automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )
    )
        # -----------------------------------
        # 7. Make sure Gemini actually
        #    returned a structured response
        # -----------------------------------

        if response.parsed is None:
            raise ValueError(
                "Gemini returned no structured response."
            )
  
        # Convert Pydantic object → dictionary
        #converts the class lyraresponse to a dictionary 
        result = response.parsed.model_dump()
        #model dump always returns a dictionary for a python object 
        return result


    except Exception as error:

        # -----------------------------------
        # 8. Prevent Brain errors from
        #    crashing Lyra
        # -----------------------------------
        error_message = str(error)

        if "503" in error_message or "UNAVAILABLE" in error_message:
          return {
            "type": "chat",
            "tool": None,
            "arguments": {},
            "answer": "I'm having a temporary issue. Please try again."
          }

        return {
        "type": "chat",
        "tool": None,
        "arguments": {},
        "answer": "I had trouble processing that request. Please try again."
        }

#wht lyra.txt does 
#How Lyra behaves
#What tools exist
#How requests should be interpreted
#What kind of responses should be returned


#json concept ....why we want gemini to return in a json type is becuase it allows your Python program to programmatically understand Gemini's output.
#json is a standard data format for communication between diff systems ...api understands json 
#using dictionary or any othe type api wont understand or  python wont understand 

