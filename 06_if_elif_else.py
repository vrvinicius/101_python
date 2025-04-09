# %%
# IF
idade = 17

if idade >= 18:
    print("Você pode dirigir!")

if idade <= 17:
    print("Você não pode dirigir!")

# %%
# IF ELSE
idade = 15

if idade >= 18:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")

# %%
# IF ELSE ELIF
idade = 85

if idade >= 80:
    print("Cuidado ao dirigir. Mantenha seu exame em dia!")
elif idade >= 18:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")

# ========
# Exercícios de fixação
# ========

# 1-
# Faça um programa que venda uma garrafa de água.
# Se o cliente escolher uma água natural, será cobrado R$ 1,50.
# Se o cliente escolher uma água com gás, será cobrado R$ 2,50.

texto = """
Escolha sua água:
(1) Água natural - R$ 1,50
(2) Água com gás - R$ 2,50
"""

opcao_agua = input(texto)

conta = 0
if opcao_agua == "1":
    conta = 1.5
elif opcao_agua == "2":
    conta = 2.5

if conta == 0:
    print("Essa opção não existe no nosso cardápio!")
else:
    print("Sua conta é de R$", conta)

# %%
# 2 -
# Adapte o Exercício 1 para considerar também a quantidade de águas compradas

texto = """
Escolha sua água:
(1) Água natural - R$ 1,50
(2) Água com gás - R$ 2,50
"""

opcao_agua = input(texto)

valor_item = 0

if opcao_agua == "1":
    valor_item = 1.5
elif opcao_agua == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Essa opção não existe no nosso cardápio!")
else:
    qtde_garrafas = input("Quantas garrafas?")
    qtde_garrafas = int(qtde_garrafas)

    conta = valor_item * qtde_garrafas

    print("Sua conta é de R$", conta)
