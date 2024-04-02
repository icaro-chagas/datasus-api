import requests
import json

url = 'http://127.0.0.1:8000/ciha'

response = requests.get(url)
json_data = response.json()
status_code = response.status_code 

print(json.dumps(json_data, indent=1))
print(status_code)