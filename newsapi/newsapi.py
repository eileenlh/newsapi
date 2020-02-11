
import requests

NEWSAPI_KEY = 'feb7de4ade3b4a6792577a028a3277a6' 
base_url = 'https://newsapi.org/v2/top-headlines'
params = {"country":"us","q":"New Hampshire",
    "apiKey": NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()
for r in result["articles"]:
    print("{}-{}".format(r["title"],r["source"]["name"]))