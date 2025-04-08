# Exemplo 1
nome = input("Qual o seu nome? ")
print("Olá,", nome,". Prazer em te conhecer!")

# %%
# Exemplo 2
numero = input("Insira um número para encontrar o seu dobro: ")
numero = int(numero) # função input retorna string. necessário conversão.

dobro = numero * 2

print("O dobro de", numero, "é:", dobro)

# %%
# Exemplo 3
# ==============
# Crie uma história simples.
# Adicione essa história em um programa.
# A cada parágrafo, a história deve aguardar o usuário apertar “enter” para dar continuidade.
# ==============

paragrafo_1 = "Era uma vez, a chapeuzinho vermelho. Ela queria muito aprender sobre Docker."
paragrafo_2 = "Ela não sabia paragrafo_or onde começar. Então conheceu a LinuxTips!"
paragrafo_3 = "Foi a melhor escolha que ela poderia ter feito. Aprendeu demais!"
paragrafo_4 = "Hoje, ela é referência na área de DevOps. Onde tudo começou lá atrás na LinuxTips"

input(paragrafo_1)
input(paragrafo_2)
input(paragrafo_3)
input(paragrafo_4)

# %%
