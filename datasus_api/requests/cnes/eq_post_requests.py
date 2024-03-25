import requests

list_params = [('RJ', '2024', '1')]

url = 'http://127.0.0.1:8000/cnes/eq'

for params in list_params:
    new_url  = f'{url}?uf={params[0]}&year={params[1]}&month={params[2]}'
    requests.post(new_url)