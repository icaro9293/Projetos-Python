import os

# encontra o caminho completo, nome, quantidade de arquivos e tamanho do arquivo digitado pelo usuario.


def formatar_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'.replace('.', ',')


try:
    # '/Users/icaro/OneDrive/Área de Trabalho/Musica'
    caminho_procura = input('digite um caminho: ')
except SyntaxError as e:
    print('erro de sintaxe. Use / ao inves de " \ " ')

termo_procura = input('digite um termo: ')  # 'opeth'
contador = 0


# percorre todos os arquivos da pasta.
for raiz, diretorio, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:  # percorrer arquivo por arquivo.
        if termo_procura in arquivo:
            try:
                contador += 1
                # armazena o caminho completo('raiz') de cada arquivo.
                caminho_completo = os.path.join(raiz, arquivo)
                # print(caminho_completo)
                # separa o nome do formato de cada arquivo em uma lista, coloca o primeiro elemento em 'nome_arquivo', e o segundo elemento em 'formato_arquivo'.
                nome_arquivo, formato_arquivo = os.path.splitext(arquivo)
                # print(nome_arquivo, formato_arquivo, sep='--')
                # print(arquivo)
                # retorna o tamanho do arquivo em bytes, precisa de uma função para converter.
                tamanho_arquivo = os.path.getsize(caminho_completo)
                print(f'arquivo encontrado: {arquivo}')
                print(f'caminho completo: {caminho_completo}')
                print(f'nome do arquivo: {nome_arquivo}')
                print(f'formato do arquivo: {formato_arquivo}')
                print(f'tamanho do arquivo: {tamanho_arquivo}')
                print(
                    f'tamanho do arquivo formatado: {formatar_tamanho(tamanho_arquivo)}')
            except FileNotFoundError as e:
                print('arquivo não encontrado.')
            except Exception as e:
                print(f'erro desconhecido: {e}')
print(f'total de arquivos encontrados: {contador}')
