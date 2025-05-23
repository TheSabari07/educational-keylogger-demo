import streamlit as st
import requests
from pymongo import MongoClient


API_URL = "http://localhost:5008"


mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client.keylogger
mongo_logs = mongo_db.logs

st.title("Keylogger Log Viewer")

view = st.radio("View logs from:", ["SQLite (Flask API)", "MongoDB (Direct)"])

if view == "SQLite (Flask API)":
    if st.button("Refresh Logs"):
        try:
            response = requests.get(f"{API_URL}/logs")
            if response.status_code == 200:
                logs = response.json()
                for log in logs:
                    st.write(f"🕒 {log[0]} - 📝 {log[1]}")
            else:
                st.error("Failed to fetch logs from Flask")
        except Exception as e:
            st.error(f"Error: {e}")

elif view == "MongoDB (Direct)":
    if st.button("Refresh Logs"):
        try:
            logs = list(mongo_logs.find().sort("timestamp", -1))
            for log in logs:
                st.write(f"🕒 {log['timestamp']} - 📝 {log['log_data']}")
        except Exception as e:
            st.error(f"MongoDB Error: {e}")
