import requests
import time
import threading
from flask import Flask
‌
# --- تنظیمات اصلی ---
TOKEN = "864658794:LtCVR4dSj3Lp5e7HR4XV-1XQOSTQoB934so"
BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}"
‌
app = Flask(name)
‌
@app.route("/")
def home():
return "Bot is running!"
‌
def send_message(chat_id, text):
try:
url = f"{BASE_URL}/sendMessage"
payload = {"chat_id": chat_id, "text": text}
requests.post(url, json=payload)
except Exception as e:
print(f"Error sending message: {e}")
‌
def run_bot():
print("Dastyar roshan shod... (Bot started)")
offset = 0
while True:
try:
url = f"{BASE_URL}/getUpdates"
params = {"offset": offset + 1, "timeout": 30}
r = requests.get(url, params=params, timeout=35)
‌
if r.status_code == 200:
updates = r.json().get("result", [])
for upd in updates:
offset = upd["update_id"]
msg = upd.get("message", {})
chat_id = msg.get("chat", {}).get("id")
text = msg.get("text", "")
‌
if chat_id:
if text == "/start":
send_message(chat_id, "سلام! من دستیار هوشمند تو هستم 😊")
elif text:
send_message(chat_id, f"پیام شما یادداشت شد: {text}")
‌
except Exception as e:
print(f"Error in loop: {e}")
‌
time.sleep(1)
‌
if name == "main":
threading.Thread(target=run_bot, daemon=True).start()
app.run(host="0.0.0.0", port=10000)
