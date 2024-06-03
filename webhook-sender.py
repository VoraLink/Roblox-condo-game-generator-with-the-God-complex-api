import requests
import time

webhook_url = "YOUR URL WEBHOOK"
last_url = ""

while True:
    try:
        response = requests.get("https://condogame.fun/api/latest")
        response.raise_for_status()
        new_url = response.json().get('url')

        if new_url and new_url != last_url:
            embed = {
                "title": "Condo Uploaded!",
                "description": new_url,
                "color": 5814783,  # Hex color code for a nice blue color
                "fields": [
                    {
                        "name": "How to get key?",
                        "value": "Join to [Condox](https://discord.gg/condox)",
                        "inline": False
                    }
                ]
            }
            requests.post(webhook_url, json={"embeds": [embed]})
            last_url = new_url
        else:
            print("No changes to the URL")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError:
        print("Unexpected response structure")
    time.sleep(5)
