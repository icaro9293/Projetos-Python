import os
import shutil
from datetime import datetime

from PIL import Image  # obtem informações do arquivo fotos.


class OrganizadorDeFotos:
    # extensões que serão manipuladas.
    extensoes = ['jpg', 'jpeg', 'JPG', 'JPEG']

    # função para criar/mover o diretorio do ano referente ao arquivo.

    def caminho_diretorio_foto(self, arquivo):
        data = self.data_foto(arquivo)
        return data.strftime('%Y') + '/' + data.strftime('%Y-%m-%d')
        # return f'{data.strftime("%Y")}/{data.strftime("%Y-%m-%d")}'

    def data_foto(self, arquivo):
        # usa a biblioteca Pillow para abrir a imagem
        foto = Image.open(arquivo)
        info = foto._getexif()  # armazena a informação de data na variavel info
        if 36867 in info:  # 36867 é relativo a data de criação, caso não contenha, é armazenado a data a partir da data de modificação obtida pela biblioteca os.
            data = info[36867]
            data = datetime.strptime(data, '%Y:%m:%d %H:%M:%S')
        else:
            data = datetime.fromtimestamp(os.path.getmtime(arquivo))
        return data

    def mover_foto(self, arquivo):
        # pasta recebe o diretorio obtido com esta função
        nova_pasta = self.caminho_diretorio_foto(arquivo)
        if not os.path.exists(nova_pasta):  # verifica se a pasta ja existe.
            os.makedirs(nova_pasta)
        # move o arquivo para a pasta desejada.
        shutil.move(arquivo, nova_pasta + '/' + arquivo)

    # função para percorrer os arquivos de uma pasta e filtrar apenas as extensões desejadas.
    def organizar(self):
        fotos = [
            # filtra os arquivos com final '.extensoes' e armazena na lista 'fotos'
            nome_arquivo for nome_arquivo in os.listdir('.') if any(nome_arquivo.endswith(ext) for ext in self.extensoes)
        ]
        for nome_arquivo in fotos:
            self.mover_foto(nome_arquivo)


# print(mover_foto('be_lakor_wallpaper_by_deathride69_d2eicxc-fullview.jpg'))
Iniciar = OrganizadorDeFotos()
Iniciar.organizar()
