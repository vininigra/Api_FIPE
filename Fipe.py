import requests

url_marcas = "https://parallelum.com.br/fipe/api/v1/carros/marcas"

req_marcas = requests.get(url_marcas)

if req_marcas.status_code == 200:
    marcas = req_marcas.json()
    for marca in marcas:
        print(marca['nome'])
        
        url_modelos = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca['codigo']}/modelos"
        req_modelos = requests.get(url_modelos)
        
        if req_modelos.status_code == 200:
            modelos = req_modelos.json()['modelos']
            for modelo in modelos:
                print(f"  - {modelo['nome']}")
                
                url_ano_modelo = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca['codigo']}/modelos/{modelo['codigo']}/anos"
                req_ano_modelo = requests.get(url_ano_modelo)
                
                if req_ano_modelo.status_code == 200:
                    anos_modelo = req_ano_modelo.json()
                    for ano_modelo in anos_modelo:

                        url_valor = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca['codigo']}/modelos/{modelo['codigo']}/anos/{ano_modelo['codigo']}"
                        req_valor = requests.get(url_valor)
                        
                        if req_valor.status_code == 200:
                            valor = req_valor.json()['Valor']
                            print(f"    - {ano_modelo['nome']}: {valor}")
elif req_marcas.status_code == 404:
    print('Não encontrado')

