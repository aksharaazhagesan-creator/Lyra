from brain.llm import ask_llm
from dispatcher import execute
from speech import speak
from web.search import web_search


def route(command):

    response = ask_llm(command)

    if response["type"] == "tool":

        execute(
            response["tool"],
            response["arguments"]
        )

    elif response["type"] == "chat":

        speak(response["answer"])

    elif response["type"] == "web":

        web_search(
            response["arguments"]["query"],
            response["arguments"]["site"]
      )

    else:

        speak("I don't know how to handle that request.")