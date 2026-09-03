import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def envoyer_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
        },
        timeout=15
    )

if __name__ == "__main__":
    envoyer_message(
        "🤖 CROUS Strasbourg Alert est bien connecté !\n\n"
        "🏠 Studios et chambres\n"
        "💰 Maximum : 520 €\n"
        "📍 Strasbourg + Schiltigheim\n"
        "⚡ Alertes immédiates"
    )
