# KeyLogger – Python + Flask + MongoDB

This project is a simple keylogger built using Python and Flask, designed to log keystrokes and store them in a MongoDB database. A minimal Flask web server is used to receive the logged data.

> Disclaimer: This keylogger is built strictly for educational and ethical use only. Unauthorized usage of keyloggers on devices without consent is illegal and unethical.

---

## How It Works

- A Python script runs in the background, recording keystrokes.
- Each keystroke is sent to a local Flask server via HTTP POST.
- The Flask server receives and stores the data in a MongoDB database.
- MongoDB acts as a backend storage to keep a persistent log of all keystrokes.

---

## Technologies Used

- Python – for capturing keystrokes and sending data
- Flask – to create a local server that receives logs
- MongoDB – to store keystroke data
- pynput – for detecting keyboard input
- requests – to send keystroke data to the server

---

## Project Flow

1. `keylogger.py`:
   - Runs on the client machine.
   - Captures keystrokes using `pynput`.
   - Sends each keystroke to the Flask server as JSON.

2. `server.py`:
   - A Flask application that exposes a POST endpoint (`/log`).
   - Stores received data in the `logs` collection of MongoDB.

---

## Example MongoDB Document

```json
{
  "_id": "ObjectId",
  "keystroke": "a",
  "timestamp": "2025-05-08T11:22:33.444Z"
}


