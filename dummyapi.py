import requests

url = "httpsapis.paralleldots.com/v3/ner"

payload = {}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
