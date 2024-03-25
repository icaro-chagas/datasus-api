import requests


list_params = [('BA', '2022', '2'), ('MG', '2020', '3'), ('CE', '2018', '5'), ('PB', '2020', '8'), ('SP', '2022', '8')]

url = 'http://127.0.0.1:8000/cnes/pf'

for params in list_params:
    new_url  = f'{url}?uf={params[0]}&year={params[1]}&month={params[2]}'
    requests.post(new_url)