import json
import os

# Deine Webhook-URL dient hier als Referenz für den Bot-Feed
WEBHOOK_URL = "https://discord.com/api/webhooks/1475534909396226210/ydfuZecOaDSGAYQHeX7WUfPi-ylPlRhvh_WncpFTy4VAA631MaF7KMssbyuYSfCmsfB_"

def update_html_with_new_drop(brand, name, price, resell, img):
    file_path = 'index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Neues Item-Objekt erstellen
    new_item = {
        "id": 99, 
        "brand": brand, 
        "name": name, 
        "price": price, 
        "resell": resell, 
        "img": img, 
        "channel": "#webhook-feed", 
        "time": "Gerade eben"
    }

    # Wir fügen das Item technisch in die Liste im JavaScript-Teil ein
    # (Dies ist eine einfache Lösung für "Nur-GitHub")
    marker = "const items = ["
    new_content = content.replace(marker, f"{marker}\n            {json.dumps(new_item)},")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    # Beispiel-Aufruf: Wenn der Bot etwas findet, führt er das hier aus
    update_html_with_new_drop("Gucci", "Messenger Bag", 140, 480, "https://via.placeholder.com/400")
