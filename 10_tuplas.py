# %%
# tupla é uma lista imutável

dados_vini = [26, 0, "solteiro", "analista de dados"]
dados_vini.append("3500.00") # inserindo novo elemento na lista
dados_vini

# %%
# tupla_vini = 26, 0, "solteiro", "analista de dados"
tupla_vini = (26, 0, "solteiro", "analista de dados", ["estagiario", "auxiliar adm"])
print(type(tupla_vini))
print(tupla_vini)

# %%
tupla_vini[-1].append("assistente adm") # não posso trocar os elementos da tupla, mas se eu tiver dentro da tupla um objeto mutável, dá pra alterar
tupla_vini

