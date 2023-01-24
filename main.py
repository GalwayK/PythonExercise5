import requests
import json

url = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-24&sortBy=publishedAt&apiKey=d81785cd88a748cab6f18bf24d97" \
      "f219"
api_key = "d81785cd88a748cab6f18bf24d97f219"

request = requests.get(url=url)
content = request.json()

print(content["articles"])
for article in content["articles"]:
    article
    print(article["title"])
    print(article["description"])
    print("\n")
print(type(content))

