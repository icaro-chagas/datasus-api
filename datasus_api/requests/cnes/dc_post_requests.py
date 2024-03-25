import requests

list_params = [('BA', '2021', '2'), ('PE', '2023', '2'), ('PB', '2013', '8'), ('CE', '2021', '8')]

url = 'http://127.0.0.1:8000/cnes/dc'

for params in list_params:
    new_url  = f'{url}?uf={params[0]}&year={params[1]}&month={params[2]}'
    requests.post(new_url)