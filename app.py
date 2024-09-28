""""""
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = './Nova Pasta Atenção/'
caminho_arquivo += 'arquivo.txt'


"""


#arquivo = open(caminho_arquivo, 'w')
##
#arquivo.close()

# Context manager
with open(caminho_arquivo, 'w+') as arquivo:
    print('Lendo na 1° abertura')
    #Escreve
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    #Lê
    arquivo.seek(0, 0) #Move pro topo do arquivo
    print(arquivo.read())
    #Lendo uma linha só
    arquivo.seek(0, 0)
    print(arquivo.readline())

print('#'*10)
with open(caminho_arquivo, 'r') as arquivo:
    print('Lendo na 2° abertura')

    print(arquivo.read())
"""


"""
#Modos de abertura de arquivo e encoding com with open

import os

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    print('Rodando o arquivo')
    #Escreve
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

#Remover ou apagar o arquivo
os.unlink(caminho_arquivo)
#Renomear o arquivo
os.rename(caminho_arquivo,'novo_nome_arq.txt')

"""