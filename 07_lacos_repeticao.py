# while condicao: #enquanto condicão for satisfeira, while permanecerá
#     print("Entrei no laço")

# %%
count = 1
while count <= 10:
    print("Laço", count)
    count = count + 1

# %%
# =========
# Tabuada do 2, iniciando em 1 até 100
# ========= 
numero = 2
count = 1

while count <= 100:
    print(numero, "x", count, "=", numero * count)
    count += 1 # count = count + 1

print("Tabuada completa!")

# %%
# =======
# Números divisíveis por 4 em um intervalo de 4 até 100
# =======

count = 4
while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)

    count += 1
# %%
# ========
# Faça um programa que recebea 4 alturas usando um laço e some-as
# ========

soma = 0 
qtde_entradas = 4

while qtde_entradas > 0:
    altura = input("Insira uma altura: ")
    altura = float(altura)
    soma += altura
    qtde_entradas -= 1 # reduz a quantidade de entradas a cada laço

print("Soma das alturas:", soma)
# %%
# ================
# Faça um programa que receba uma quantidade indefinida
# de valores correspondentes a “saldo em conta”,
# mas quando o usuário apertar “enter” sem digitar valor algum,
# o programa para de receber valores, e exibe a soma
# de todos os valores digitados anteriormente.
# =================

saldo_total = 0

while True: #while infinito
    saldo = input("Digite seu saldo: ")
    if saldo == "":
        break # forçar a saída do while

    saldo_total += float(saldo)

print("Saldo total:", saldo_total)


# FOR (percorre os elementos de um objeto)
# %%
nome = "Vinícius Vieira"

for letra in nome:
    print(letra)


# %%
# tabuada usando for

numero = 2
max_numero = 100

for i in range(1, max_numero + 1):
    print(numero, "x", i, "=", numero * i)

# %%
# divisiveis por 4

for i in range(4, 101):
    if i % 4 == 0:
        print(i)
# %%
# soma das alturas
soma = 0
qtde_entradas = 4

for i in range(qtde_entradas):
    altura = input("Insira uma altura: ")
    altura = float(altura)
    soma += altura

print("Soma das alturas:", soma)