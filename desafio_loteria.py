# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

# %%

import random

def valid_jogada():
    while True:
        try: 
            jogada = int(input("Digite um número: "))

        except ValueError as err:
            print("Sua jogada não é válida!")
            continue

        if 1 <= jogada <= 15:
            return jogada
          
        print("Sua jogada não é válida!")

def valid_status(numero_sorteio, jogada):        
    if numero_sorteio == jogada:
        print("Você ganhou, parabéns!")
        return True

    elif jogada > numero_sorteio:
        print("O número é menor do que sua jogada!")
        return False
            
    else:
        print("O número é maior do que sua jogada!")
        return False

numero_sorteio = random.randint(1, 15)

for i in range(3):

    jogada = valid_jogada()
    if valid_status(numero_sorteio=numero_sorteio, jogada=jogada):
        break

else: # se o for encerrar com sucesso, sem ter um break no caminho, também executa esse else
    print("Suas tentativas acabaram!")