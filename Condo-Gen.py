import requests
import time
import os

webhook_url = ("THE-URL-OF-YOUR-WEBHOOK")

last_url = ""

while True:
  try:
    response = requests.get("https://condogame.fun/api/latest")
    new_url = response.json()['url']

    if new_url != last_url:
      # Send the new URL to Discord
      requests.post(webhook_url, json={"content": new_url})
      # Update the last URL
      last_url = new_url
    else:
      print(
          "No changes to the URL"
      )
  except:
    print("There was an error fetching at https://condogame.fun/api/latest")
  time.sleep(5)
