from datetime import datetime
from ai import AI

jarvis = AI()

command = ""

while True and command != "goodbye":
    command = jarvis.listen()
    print("Command was:", command)

    if command in ["hello", "hi"]:
        jarvis.say("Hello sir, how can I be of assistance?")
    if command in ["morning", "afternoon", "evening"]:
        now = datetime.now()
        hr = now.hour
        if hr <= 0 <=12:
            message = "Morning"
        if hr >=12 <= 17:
            message = "Afternoon"
        if hr >=17 <=21:
            message = "Evening"
        if hr > 21: message = "Night"

        message = "Good " + message + " sir"
        jarvis.say(message)