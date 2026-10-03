import asyncio
import edge_tts
import speech_recognition as sr
import tempfile
import os
import subprocess

recognizer = sr.Recognizer()


def speak(text):
    asyncio.run(_speak(text))


async def _speak(text):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        filename = temp_audio.name

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-JennyNeural"
    )

    await communicate.save(filename)

    # Use macOS's native audio player
    subprocess.run(["afplay", filename])

    os.remove(filename)


def listen():

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5)

            command = recognizer.recognize_google(audio)

            print(f"You said: {command}")

            return command.lower()

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None

        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return ""

        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return ""