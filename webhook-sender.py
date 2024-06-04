import requests
import time

webhook_url = "webhook_URL"
last_url = ""

while True:
    try:
        response = requests.get("https://condogame.fun/api/latest")
        response.raise_for_status()
        new_url = response.json().get('url')
        
        key_response = requests.get("https://condogame.fun/api/key")
        key_response.raise_for_status()
        key = key_response.json().get('key')

        if new_url and new_url != last_url:
            embed = {
                "title": "¡Condo Found!",
                "description": new_url,
                "color": 5814783,
                "fields": [
                    {
                        "name": "The Key is",
                        "value": f"{key}",
                        "inline": False
                    }
                ],
                "image": {
                    "url": "https://media1.tenor.com/m/oNzbYT8uZj4AAAAC/tbh-white-creature.gif"
                }
            }
            requests.post(webhook_url, json={"embeds": [embed]})
            last_url = new_url
        else:
            print(" ")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError:
        print("Unexpected response structure")
    time.sleep(5)
