import requests
import json
response_API = requests.get("http://127.0.0.1:8000/api/profile/?format=json")
data = response_API.text
# print(data)
print(json.loads(data))
# info = parse_json['1']
# print("Info about API:\n", info)