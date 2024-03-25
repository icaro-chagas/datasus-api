import requests
import json

#url = 'http://127.0.0.1:8000/siasus/pa?page_number=6&year=2023&uf=SP&month=12'
#url = 'http://127.0.0.1:8000/siasus/pa?page_number=6&year=2021'
url = 'http://127.0.0.1:8000/siasus/pa?uf=sp'

response = requests.get(url)
json_data = response.json()
status_code = response.status_code 

print(json.dumps(json_data, indent=1))
print(status_code)