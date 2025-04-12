# %%

# Forma 1
idades = [28, 42, 43, 35, 39, 20]

print(idades)

# %%
# nome, sobrenome, idade, casado, renda
vini = ["Vinicius", "Vieira", 26, False, 2500.53] # uma lista pode ter elementos de diferentes tipos

print(vini)

# %%
# acessando uma lista

#idade
print(vini[2])

# renda
print(vini[4])

# %%
# Manipulando listas
idades = [28, 42, 43, 35, 39, 20]

print("Soma das idades: ", sum(idades))

print("Quantidade de idades: ", len(idades))

print("Média das idades: ", sum(idades) / len(idades))

print("Menor idade: ", min(idades))

print("Maior das idades:", max(idades))

# %%

vini = ["Vinicius",
        "Vieira",
        26,
        False,
        ["Estagiário", "Auxiliar", "Analista"],
        [900, 1530, 3400]]


print(len(vini))

vini[4][0] #acessando o primeiro elemento da lista, que é o quarto elemento da variavel 'vini' (índice inicia em 0)


# %%
# navegando sem saber o tamanho da lista
# quero pegar o primeiro salario. Não sei quantos elementos tem na lista, mas sei que o salário é o último elemento da lista

tamanho = len(vini)
pos = tamanho - 1 # pegando o tamanho da lista e subtraindo um, visto que começa no índice 0
vini[pos]

# acessando o ultimo salário

salarios = vini[pos]
vini[pos][len(salarios) - 1]

# %%
vini[-1] # atalho para acessar o último elemento da lista
vini[-2] # atalho para acessar o penúltimo elemento da lista

vini[-1][-1] # acessando o último salário de outra forma

# %%
# acessando N elementos da lista

vini[0:3]
vini[:3]
# %%

# acessando os dois últimos cargos
# %%
vini[4]

vini[4][1:3]
vini[4][-2:] # melhor forma

# vini[ start : stop ]

# %%
# acessando os salários do último para o primeiro

salarios = vini[5]
salarios[::-1]

# pegando o primeiro, pulando o segundo, até o terceiro
salarios[::2]

# vini[ start : stop: step ]

# %%
# =====================
# Escreva um programa que receba uma lista de números
#  do usuário e conte quantas vezes um número
# específico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.
# =====================

lista = [1,2,3,3,3,1,2,6,4,4,3,32,8,7]

numero = int(input("Digite um número: "))

contador = 0
for i in lista:
    if i == numero:
        contador += 1

print("Quantidade de", numero, ":", contador)

# %%
# métodos da lista

##### LISTA É UM OBJETO MUTÁVEL #####

idades = [17, 32, 56, 87]
print(idades)

# adicionar novos elementos
idades.append(26)
print(idades)

# %%
idades = []

while True:
    idade = input("Digite uma idade: ")

    if idade == "":
        break

    idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("MEDIA:", media)
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTDE:", qtde)