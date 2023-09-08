import requests

api_key = "16ce1aebadac4264b428a357dc1f59de"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-08-08&sortBy=publishedAt&apiKey=16ce1aebadac4264b428a357dc1f59de"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
