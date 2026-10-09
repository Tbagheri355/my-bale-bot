import requests
import time
from flask import Flask

TOKEN = "864658794:LtCVR4dSj3Lp5e7HR4XV-1XQOSTQoB934so"
BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def send_message(chat_id, text):
    try:
        url = f"{BASE_URL}/sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

def check_updates():
    print("Checking for messages...")
    offset = 0
    try:
        url = f"{BASE_URL}/getUpdates"
        params = {"offset": offset + 1, "timeout": 20}
        r = requests.get(url, params=params, timeout=25)
        if r.status_code == 200:
            updates = r.json().get("result", [])
            for upd in updates:
                msg = upd.get("message", {})
                chat_id = msg.get("chat", {}).get("id")
                text = msg.get("text", "")
                if chat_id:
                    if text == "/start":
                        send_message(chat_id, "Hello! I am your bot.")
                    elif text:
                        send_message(chat_id, f"You said: {text}")
    except Exception as e:
        print(f"Update error: {e}")

if __name__ == "__main__":
    check_updates()
    app.run(host="0.0.0.0", port=10000)
