import requests
import time
import threading
from flask import Flask

TOKEN = "864658794:ltCVR4dSj3Lp5e7HR4XV-1XQOSTQoB934so"
BASE = "https://tapi.bale.ai/bot" + TOKEN

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def send(chat_id, text):
    try:
        requests.post(BASE + "/sendMessage", json={"chat_id": chat_id, "text": text}, timeout=10)
    except Exception as e:
        print("send error:", e)

def run_bot():
    offset = 0
    print("Dastyar roshan shod...")
    while True:
        try:
            r = requests.get(BASE + "/getUpdates",
                             params={"offset": offset + 1, "timeout": 30},
                             timeout=35)
            for upd in r.json().get("result", []):
                offset = upd["update_id"]
                msg = upd.get("message", {})
                chat_id = msg.get("chat", {}).get("id")
                text = msg.get("text", "")
                if not chat_id:
                    continue
                if text == "/start":
                    send(chat_id, "سلام! من دستیار هوشمند تو هستم 😊")
                elif text:
                    send(chat_id, "یادداشت شد: " + text)
        except Exception as e:
            print("error:", e)
            time.sleep(5)

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
