import json
import os
import shutil

# MOVER, COPIAR E DELETAR ARQUIVOS.
# caminho_original = r'C:\Users\icaro\Downloads\Bridge Of Spies (2015) [1080p] [YTS.AG]2'
# caminho_novo = r'C:\Users\icaro\Downloads\Bridge Of Spies (2015) [1080p] [YTS.AG]'

# try:
#     os.mkdir(caminho_novo)  #cria uma pasta.
# except FileExistsError as e:
#     print(f'a pasta {caminho_novo} ja existe.')

# for raiz, diretorio, arquivos in os.walk(caminho_original):
#     for arquivo in arquivos:
#         caminho_antigo_arquivo = os.path.join(raiz, arquivo) #pasta antiga + arquivo
#         print(caminho_antigo_arquivo)
#         caminho_novo_arquivo = os.path.join(caminho_novo, arquivo) #pasta nova + arquivo
#         print(caminho_novo_arquivo)

#         try:
#             shutil.move(caminho_antigo_arquivo, caminho_novo_arquivo) #move o arquivo para a pasta desejada.
#             print(f'arquivo {arquivo} movido com sucesso.')
#             # shutil.copy(caminho_antigo_arquivo, caminho_novo_arquivo) #copia o arquivo.
#             # print(f'arquivo {arquivo} foi copiado com sucesso.')
#             os.remove(caminho_novo_arquivo) #remove o arquivo da pasta.
#         except:
#             print('ERRO')
# ------------------------------------------------------------------------------------------
# CRIAR, LER E ESCREVER ARQUIVOS
# try:
#     # 'w' write para poder escrever o arquivo, '+' significa leitura e escrita.
#     arquivo = open('testando.txt', 'w+')
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.write('Linha 3\n')

#     #o cursor de leitura fica no fim do arquivo após escrever, então para ler preciso voltar o cursor para o inicio
#     arquivo.seek(0, 0) # 1o é o offset.
#     print(arquivo.read()) #le todo o arquivo de uma vez
#     print('=-'*30)

#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='') #le linha por linha
#     print(arquivo.readline(), end='')
#     print(arquivo.readline(), end='')
#     print('=-'*30)

#     arquivo.seek(0, 0)
#     print(arquivo.readlines()) #le e coloca numa lista.
#     arquivo.seek(0, 0)
#     for linha in arquivo: #for linha in arquivo.readlines() também funciona
#         print(linha, end='')
# finally:
#     arquivo.close()

# ESTA É A FORMA MAIS ADEQUADA DE MANIPULAR O ARQUIVO, POIS NÃO PRECISA MANDAR FECHAR 'close()'

# with open('testando.txt', 'w+') as arquivo:
#     arquivo.write('linha 1\n')
#     arquivo.write('linha 2\n')
#     arquivo.write('linha 3\n')
#     arquivo.seek(0, 0)
#     print(arquivo.read())
# with open('testando.txt', 'a+') as arquivo: # 'a' é como um APPEND, adiciona na lista sem apagar. Se fosse 'w+', iria apagar tudo do arquivo e escrever o comando desejado. 'r' é apenas para ler o arquivo.
#      arquivo.write('outra linha\n')
#      arquivo.seek(0, 0)
#      print(arquivo.read())
# os.remove('testando.txt')

# CRIANDO UM ARQUIVO JSON E ADICIONANDO UM DICIONARIO

d1 = {
    'Pessoa 1': {
        'nome': 'Cleiton',
        'idade': 25
    },
    'Pessoa 2': {
        'nome': 'Clone',
        'idade': 30
    }
}
print(d1)
d1_json = json.dumps(d1, indent=True)
print(d1_json)
# 'w+' pois quero que apague e crie de novo caso ja exista.
with open('testando.json', 'w+') as arquivo:
    arquivo.write(d1_json)

with open('testando.json', 'r') as arquivo:  # ler o arquivo
    d1_json = json.loads(d1_json)  # volta a ler como um dicionario

for k, v in d1_json.items():
    print(k)
