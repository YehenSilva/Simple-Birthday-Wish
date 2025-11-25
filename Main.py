import pyttsx3
import time

def wish(name):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Words per minute

    # Lines of the song
    lines = [
        "Happy Birthday to You",
        "Happy Birthday to You",
        f"Happy Birthday Dear {name}",
        "Happy Birthday to You"
    ]

    # Print and speak each line
    for line in lines:
        print(line)
        engine.say(line)
        engine.runAndWait()
        time.sleep(0.5)  # Short pause between lines

    engine.stop()


while True:
    name=str(input("Enter the name: ")).upper( )
    type(name)==str and  name.isalpha( )

wish(name)
