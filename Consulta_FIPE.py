import urllib.request, json, pandas as pd

"""
Input = MARCA E CÓDIGO FIPE DO VEÍCULO
Exemplo : FIPE('RENAULT','025185-2')

Output = Tabela com valores
"""

def FIPE(brand,code):
    # Encontrar ID da marca:
    with urllib.request.urlopen("https://fipeapi.appspot.com/api/1/carros/marcas.json") as url:
        marcas = json.loads(url.read().decode())

        id = {}

        for i in range(len(marcas)):
            id[marcas[i]['name']] = marcas[i]['id']

    # Listar todos os anos dos modelo
    with urllib.request.urlopen(f"https://fipeapi.appspot.com/api/1/carros/veiculo/{id[brand]}/{code}.json") as url:
        data = json.loads(url.read().decode())

        year = []

    # Criar dataframe com anos e valores do veículo
        for i in range(len(data)):
            year.append(data[i]['fipe_codigo'])

    value = {}

    for j in range(len(year)):
        with urllib.request.urlopen(f"https://fipeapi.appspot.com/api/1/carros/veiculo/{id[brand]}/{code}/{year[j]}.json") as url:
            parameters = json.loads(url.read().decode())
            value[year[j]] = parameters['preco']

    values = pd.DataFrame.from_dict(value, orient='index')
    values.columns=[parameters['name']]

    return print(values)

FIPE('RENAULT','025185-2')

