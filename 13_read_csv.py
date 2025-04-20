# %%

arquivo = "data_read_test.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)


# %%
# criando um dicionário com os dados do csv
dados = dict()

chaves = lines[0].strip("\n").split(";") # strip para remover o \n. split para separar os elementos e transformar em lista

for c in chaves:
    dados[c] = [] # criando uma lista para cada chave do dicionário. a chave é o cabeçalho do arquivo csv


# %%

for l in lines[1:]: # primeira linha (cabeçalho) é a chave. pegando valores a partir da linha 1
    
    valores = l.strip("\n").split(";") # criando lista com os valores
    
    for i in range(0, len(valores)): # percorrendo a quantidade de chaves do dicionário
        dados[chaves[i]].append(valores[i]) # pegando os valores da posição i e atribuindo à chave na posição i

# %%

idades = []

for i in dados["idade"]:
    idades.append(int(i))

media_idades = sum(idades) / len(idades)
media_idades