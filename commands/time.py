from datetime import datetime
from speech import speak
def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")