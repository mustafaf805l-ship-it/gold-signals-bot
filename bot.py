import requests

TOKEN = "ضع_التوكن_هنا"
CHAT_ID = "ضع_الشات_آيدي_هنا"

message = """
🟢 GOLD SIGNAL

BUY XAUUSD

SL: 5$
TP: 10$
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print("Signal sent")
