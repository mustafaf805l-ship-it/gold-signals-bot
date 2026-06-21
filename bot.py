import requests

TOKEN = "8883189014:AAE3atZNKuubfS0ssoKFMl4loZAzQma14E0"
CHAT_ID = "967764129"

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
