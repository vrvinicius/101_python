# %%
# dicionarios: pares de chave/valor
# as chaves podem ser string, int e float (evitar)

dados_vini = {
    "nome":"Vinicius",
    "sobrenome": "Vieira",
    "filhos":False,
    "formacao":["economia", "analise estrategica de dados"],
    "cargos":[
        {"empresa":"sicredi", "cargo":"estagiario"},
        {"empresa":"sicredi", "cargo":"analista de dados"},
        {"empresa":"sicredi", "cargo":"analista de dados iii"}
    ]
}

# %%
# acessando uma chave
print(dados_vini["nome"])

# acessando a ultima formacao (ultimo elemento da lista)
print(dados_vini["formacao"][-1])

#ultima empresa
print(dados_vini["cargos"][-1]["empresa"])

# %%

# inserindo novas chaves no dicionário
dados_vini["estado civil"] = "solteiro"

# %%

# descobrindo as chaves e valores do dicionário

print("Chaves:", dados_vini.keys())
print("Valores:", dados_vini.values())
print("Items:", dados_vini.items())

# %%
# percorrendo pelo dicionário
for i in dados_vini:
    print(i, ">", dados_vini[i]) # i traz só chaves. dados_vini[i] acessa os valores das chaves

# %%

for chave, valor in dados_vini.items():
    print(chave, ">", valor)



# ----------
#  Exercícios de fixação
# ----------

# %%
# Faça um programa que o usuário insira o nome de uma fruta e retorne o seu valor
fruta = input("Entre com o nome da fruta:")

frutas = {
    "Pera": "R$1,25",
    "Goiaba": "R$2,15",
    "Abacaxi": "R$3,20",
    "Jaca": "R$5,80",
    "Laranja": "R$0,65",
    "Limão": "R$1,25",
    "Maçã": "R$1,50",
    "Banana": "R$2,75",
    "Uva": "R$1,90",
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Não temos essa fruta no nosso estoque!")

# %%
# Escreva um programa que solicite ao usuário frases.
# Para parar de solicitar frases, pressionar "enter".
# O programa deve apresentar cada frase e quantas vezes ela foi repetida.
# Ordene por quantidade decrescente

frases = {}

while True:
    frase = input(" Digite uma frase: ")
    if frase == "":
        break

    if frase not in frases:
        frases[frase] = 1 # cria um chave no dicionário com o valor da frase
    else:
        frases[frase] += 1

items = list(frases.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    print(i, ">", j)



# %%
# ordenacao
dados = {
    "oi":1,
    "ola": 10,
    "oi tudo bem":3,
    "teste":5
}

itens = list(dados.items())
itens.sort(key=lambda x: x[-1], reverse=True) # ordenando conforme o ultimo elemento de cada tupla, que, nesse caso, sao os valores

for i, j in itens:
    print(i, ">", j)