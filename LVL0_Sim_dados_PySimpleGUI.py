import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.mensagem = 'voce gostaria de gerar um novo valor para o dado (S/N):  '
    #DEFININDO O LAYOUT
        self.layout = [
        [sg.Text('Jogar o dado?')],
        [sg.Button('Sim'), sg.Button('Não')]
        ]


    def Iniciar(self):
        # CRIANDO UMA JANELA
        self.janela = sg.Window('Simulador de Dados', layout = self.layout)
        #LER OS VALORES DA TELA
        self.eventos, self.valores = self.janela.Read()
        #FAZER ALGUMA COISA COM OS VALORES
        if self.eventos == 'Sim':
            valor = self.GerarValorDado()
            print(valor)
        elif self.eventos == 'Não':
            print('obrigado')
            
            
    def GerarValorDado(self):
        return random.randint(1, 6)


sim = SimuladorDeDado()
sim.Iniciar()
