### `birthday_wisher.py`

```python
import pyttsx3
import time

def wish(name):
    """
    Wishes a person Happy Birthday by printing and speaking the song line by line.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Words per minute

    # Lines of the birthday song
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


def main():
    print("=== Birthday Wisher ===")
    while True:
        name = input("Enter the name (or type 'exit' to quit): ").strip()
        if name.lower() == "exit":
            print("Goodbye!")
            break
        elif name.isalpha():
            name_upper = name.upper()
            wish(name_upper)
        else:
            print("Please enter a valid name (letters only).")


if __name__ == "__main__":
    main()
```

---

### `README.md`

````markdown
# Birthday Wisher - Python Text-to-Speech

A simple Python program that wishes someone a Happy Birthday using text-to-speech. It prints the birthday song line by line and reads it aloud using the `pyttsx3` library.

## Features

- Reusable function to wish anyone by name.
- Speaks the song line by line with pauses for a natural effect.
- Converts the entered name to uppercase for consistency.
- Continuously asks for names until the user exits.
- Easy to extend for other greetings.

## Requirements

- Python 3.x
- `pyttsx3` library

Install the library using pip:

```bash
pip install pyttsx3
````

## Usage

1. Clone this repository:

```bash
git clone <repository_url>
```

2. Run the Python script:

```bash
python birthday_wisher.py
```

3. Enter a name when prompted, and the program will wish them a Happy Birthday aloud. Type `exit` to quit.

## Example

```
Enter the name: Yehen
HAPPY BIRTHDAY TO YOU
HAPPY BIRTHDAY TO YOU
HAPPY BIRTHDAY DEAR YEHEN
HAPPY BIRTHDAY TO YOU
```

## License

This project is open-source and available under the MIT License.

```

---

This version:  
- Has a reusable `wish()` function.  
- Continuously prompts for names until the user types `exit`.  
- Converts names to uppercase.  
- Comes with a ready-to-use README for GitHub.  

If you want, I can **also make the song repeat the first two lines exactly like the classic birthday tune**, so it sounds more natural when spoken. Do you want me to do that?
```
