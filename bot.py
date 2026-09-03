import os
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://trouverunlogement.lescrous.fr/tools/47/search"


def envoyer_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
        },
        timeout=15
    )

    response.raise_for_status()


def rechercher_logements():
    response = requests.get(
        URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    logements = []

    for lien in soup.find_all("a", href=True):
        href = lien["href"]

        if "/accommodations/" not in href:
            continue

        texte = lien.get_text(" ", strip=True)

        if texte:
            logements.append(
                f"🏠 {texte}\n"
                f"https://trouverunlogement.lescrous.fr{href}"
            )

    return list(dict.fromkeys(logements))


if __name__ == "__main__":
    logements = rechercher_logements()

    envoyer_message(
        f"🔎 Test CROUS Strasbourg\n\n"
        f"Nombre de logements trouvés : {len(logements)}"
    )
