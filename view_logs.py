import tkinter as tk
import sqlite3

def show_logs():
    conn = sqlite3.connect('keylogger.db')
    c = conn.cursor()
    c.execute("SELECT * FROM logs")
    logs = c.fetchall()
    conn.close()

    window = tk.Tk()
    window.title("Keylogger Logs")

    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text = tk.Text(window, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text.pack(expand=True, fill=tk.BOTH)
    scrollbar.config(command=text.yview)

    for log in logs:
        timestamp, log_data = log
        text.insert(tk.END, f"Timestamp: {timestamp}\nLog Data: {log_data}\n\n")

    window.mainloop()

if __name__ == '__main__':
    show_logs()
