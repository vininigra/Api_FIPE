import requests

url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"

req = requests.request("GET", url)

if req.status_code == 200:
    marcas = req.json()
    print(marcas)
elif req.status_code == 404:
    print('Não encontrado')
