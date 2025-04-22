# ------
# Obtendo infos de CEPs
# ------

# %%

import requests # realizar requisições na web via api
import json # para tratar listas/dicionários em arquivos json
from tqdm import tqdm # para criar a barra de progresso / execução do programa
import pandas as pd

# %%

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863",
    "19060100",
    "58038200",
    "06694380"
]

url = "https://viacep.com.br/ws/{cep}/json/"

dados = []

for i in tqdm(ceps): # tqdm para gerar a barra de progresso do programa
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200: # status de requisicao bem sucedida
        dados.append(resposta.json())

dados

# %%
dados

# %%
# salvando os ceps num arquivo json

with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

# %%
# salvando os ceps num arquivo csv

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

# %%
