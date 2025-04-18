# %%

def f(x):
    return 1 + x

f(1)

# %%

# exemplo de cálculo de juros compostos

def juros_compostos(valor:int, taxa:float, anos:int) -> float:
    """
    juros_compostos serve para calcular o retorno financeiro a partir de um aporte.
    Deve-se considerar o valor, a taxa de juros atual (em decimal) e o tempo (em anos) para cálculo do valor futuro.
    
    aporte:
        um número inteiro que represente o valor em R$

    taxa:
        um número float entre 0 e 1 que represente o valor da taxa de juros

    anos:
        um número inteiro >= 1 que representa o tempo do investimento    
    """
    return valor * (1 + taxa) ** anos

juros_compostos(valor=1000, taxa=0.13, anos=5)

# %%
def ola_mundo(): # não necessariamente uma função precisa ter um argumento
    print("Bem vindo ao mundo do python!")

ola_mundo()


# ----------
# Exercícios de fixação
# ----------

# %%
# Faça um programa que receba um número e informe se este número é par ou ímpar

def par_impar(numero:int):
    if numero % 2 == 0:
        print("É par!")
    else:
        print("É impar!")

numero = int(input("Digite um número: "))

par_impar(numero)


# funções matemáticas
# %%
def soma(a:float, b:float) -> float:
    return a + b

def media(a:float, b:float) -> float:
    # return (a + b) / 2
    return soma(a, b) / 2


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

print("Média:", media(a, b))

# %%
# opção sem definir a quantidade de argumentos da função

def soma(a:float, b:float, *args) -> float: # * args funciona como uma lista/tupla indefinida de elementos
    valores = [a, b] + list(args) # "concatenando" as duas listas
    return sum(valores)

def media(a:float, b:float, *args) -> float:
    return soma(a, b, *args) / (len(args) + 2) # + 2 é o a + b

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))

print("Média:", media(a, b, c, d)) # incluí c e d sem precisar explicitar na função. *args faz isso

# %%
# calculando preço com imposto

def calc_imposto(preco:float, tx_imposto:float, **kwargs): # kwargs possibilita adicionar elementos nomeados de tamanho indefinido na função
    imposto = preco * tx_imposto

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

# %%

calc_imposto(100, 0.03)
# %%
calc_imposto(100, 0.03, municipal=0.01, estadual=0.03) # incluindo, além do imposto base, o municipal e o estadual (possibilitado pelo kwargs)

# %%
impostos_adicionais = {
    "municipal":0.01,
    "estadual":0.03
}

calc_imposto(100, 0.03, **impostos_adicionais)  # ** abre o dicionário como elementos apartados.

# %%
