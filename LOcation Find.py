import requests, json

ip = input()
api = "http://ip-api.com/json/"
api += ip
data = requests.get(api).content
data = json.loads(data.decode('utf-8'))

print("{data['city']}, {data['regionName']}, {data['country']}")