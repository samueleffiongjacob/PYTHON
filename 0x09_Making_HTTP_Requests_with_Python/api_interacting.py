import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})
# "Accept" : "text/plain"
data = response.json()

print(data["joke"])
print(f"status: {data['status']}")



