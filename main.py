import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "привіт",
    "body": "тест",
    "userId": 1
}

res = requests.post(url, json=data)

print(res.status_code)
print(res.json())