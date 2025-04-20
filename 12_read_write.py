# %%

# -------
# READ
# -------

# Método 1
# para arquivos de texto no mesmo diretório
nome_arquivo = "historia.txt"

# abre o arquivo em formato de leitura
open_file = open(nome_arquivo)

# lê os dados do arquivo
conteudo = open_file.read()
print(conteudo)

# fecha o arquivo
open_file.close()
# %%

# Método 2
with open(nome_arquivo) as open_file: # para não precisar inserir o comando de fechar o arquivo
    conteudo = open_file.read()
    
print(conteudo)


# -------
# WRITE
# -------
# %%

texto = "O que escreverei aqui?"

nome_arquivo = "nova_historia.txt"

with open(nome_arquivo, mode="w") as open_file: # alterar mode para sobrescrever, adicionar ao final, etc.
    open_file.write(texto)

# %%
