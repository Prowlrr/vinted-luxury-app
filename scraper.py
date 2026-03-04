import requests
import json
import os
from datetime import datetime

# 1. DEINE KONFIGURATION
WEBHOOK_URL = "https://discord.com/api/webhooks/1475534909396226210/ydfuZecOaDSGAYQHeX7WUfPi-ylPlRhvh_WncpFTy4VAA631MaF7KMssbyuYSfCmsfB_"

def scrape_vinted_simulation():
    """
    Hier würde normalerweise deine Vinted-Suche stattfinden.
    Wir erstellen hier einen Beispiel-Fund für den Test.
    """
    return {
        "brand": "Gucci",
        "name": "Vintage Monogram Messenger Bag",
        "price": 160,
        "resell": 450,
        "img": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=500",
        "link": "https://www.vinted.de/"
    }

def send_to_discord(item):
    """Sendet den Fund inklusive Resell-Wert an Discord [cite: 2026-02-23]."""
    profit = item['resell'] - item['price']
    
    payload = {
        "username": "Vinted Luxury Bot",
        "embeds": [{
            "title": f"🚨 NEUER DROP: {item['brand']}",
            "url": item['link'],
            "color": 610746, # Vinted Teal
            "fields": [
                {"name": "Produkt", "value": item['name'], "inline": False},
                {"name": "Vinted Preis", "value": f"€{item['price']}", "inline": True},
                {"name": "Est. Resell", "value": f"€{item['resell']}", "inline": True},
                {"name": "Potential Profit", "value": f"**€{profit}**", "inline": True}
            ],
            "image": {"url": item['img']},
            "footer": {"text": f"Gefunden am {datetime.now().strftime('%H:%M:%S')}"}
        }]
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("Erfolgreich an Discord gesendet!")
        else:
            print(f"Discord Fehler: {response.status_code}")
    except Exception as e:
        print(f"Fehler beim Senden: {e}")

def update_index_html(item):
    """Fügt das neue Item oben in die Liste der index.html ein [cite: 2026-02-23]."""
    file_path = 'index.html'
    
    if not os.path.exists(file_path):
        print("Fehler: index.html wurde nicht gefunden!")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Neues Item-Objekt für die JavaScript-Liste
    new_entry = {
        "id": int(datetime.now().timestamp()),
        "brand": item['brand'],
        "name": item['name'],
        "price": item['price'],
        "resell": item['resell'],
        "img": item['img'],
        "channel": "#vinted-drops",
        "time": "Gerade eben"
    }

    # Wir suchen die Stelle im Code, wo die Items anfangen
    marker = "const items = ["
    updated_content = content.replace(marker, f"{marker}\n            {json.dumps(new_entry)},")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("index.html erfolgreich aktualisiert!")

if __name__ == "__main__":
    # 1. Item "finden"
    found_item = scrape_vinted_simulation()
    
    # 2. An Discord schicken [cite: 2026-02-23]
    send_to_discord(found_item)
    
    # 3. In die App schreiben [cite: 2026-02-23]
    update_index_html(found_item)
