import requests

#list_params = [('SP', '2023', '12', 'a'), ('SP', '2023', '12', 'b')]
list_params = [('SP', '2007', '12', '')]
#list_params = [('SP', '2022', '5', 'a'), ('SP', '2021', '3', 'b')]

url = 'http://127.0.0.1:8000/siasus/pa'

for params in list_params:
    new_url  = f'{url}?uf={params[0]}&year={params[1]}&month={params[2]}&letter={params[3]}'
    requests.post(new_url)