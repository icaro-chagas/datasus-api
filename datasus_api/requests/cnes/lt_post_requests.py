import requests

#list_params = [('SP', '2023', '12', 'a'), ('SP', '2023', '12', 'b')]
# list_params = [('SP', '2023', '12', 'b')]
list_params = [('BA', '2023', '2'), ('PE', '2020', '3'), ('PB', '2018', '5'), ('CE', '2021', '8'),
               ('SP', '2023', '8'), ('SP', '2022', '8'), ('SP', '2023', '9'), ('SP', '2023', '10')]

url = 'http://127.0.0.1:8000/cnes/lt'

for params in list_params:
    new_url  = f'{url}?uf={params[0]}&year={params[1]}&month={params[2]}'
    requests.post(new_url)