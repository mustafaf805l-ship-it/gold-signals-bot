import time
import requests

# ضع بياناتك هنا
TOKEN = "8883189014:AAE3atZNKuubfS0ssoKFMl4loZAzQma14E0"
CHAT_ID = "967764129"

def get_gold_price():
    try:
        # جلب سعر الذهب المباشر مقابل الدولار من واجهة مجانية (كمثال)
        url = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
        response = requests.get(url).json()
        # عملة PAXG هي عملة مشفرة مدعومة بالذهب الحقيقي وتتحرك مع سعر أونصة الذهب تماماً
        price = float(response['price'])
        return price
    except Exception as e:
        print(f"خطأ في جلب السعر: {e}")
        return None

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

print("البوت بدأ العمل ومراقبة السوق الحية...")

# لتخزين آخر إشارة تم إرسالها منعاً للتكرار المزعج
last_signal = None

while True:
    current_price = get_gold_price()
    
    if current_price:
        print(f"السعر الحالي للذهب: ${current_price}")
        
        # هنا نضع معادلة أو شرط التحليل الفني (كمثال مبسط):
        # سنفترض أن نقطة الارتكاز اليومية هي 2350 (يمكنك تغيير هذا الرقم بناءً على تحليلك)
        pivot_point = 2350.0 
        
        if current_price > pivot_point and last_signal != "BUY":
            message = f"🟢 إشارة ذهب حقيقية\n\nشراء (BUY XAUUSD)\nالسعر الحالي: ${current_price}\n\nSL: {current_price - 5}\nTP: {current_price + 10}"
            send_telegram_message(message)
            last_signal = "BUY"
            
        elif current_price < pivot_point and last_signal != "SELL":
            message = f"🔴 إشارة ذهب حقيقية\n\nبيع (SELL XAUUSD)\nالسعر الحالي: ${current_price}\n\nSL: {current_price + 5}\nTP: {current_price - 10}"
            send_telegram_message(message)
            last_signal = "SELL"
            
    # انتظر 5 دقائق (300 ثانية) قبل فحص السعر والتحليل مرة أخرى لمنع الحظر وحفظ موارد السيرفر
    time.sleep(300)
