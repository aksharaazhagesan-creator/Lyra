from speech import listen, speak
from brain.router import route


def run():

    speak("Lyra is listening.")

    while True:

        command = listen()

        if command is None:
            speak("I didn't hear anything. Goodbye.")
            break

        if command == "":
            speak("I didn't understand. Could you repeat?")
            continue

        route(command)