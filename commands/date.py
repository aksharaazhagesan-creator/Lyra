from datetime import datetime
from speech import speak
def tell_date():
    current_date = datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {current_date}")