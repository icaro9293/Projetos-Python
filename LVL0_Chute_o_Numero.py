# import random


# class ChutarNumero:
#     def __init__(self):
#         self.mensagem = 'Tente adivinhar o número...: '
#         self.valor = 0
#         self.aleatorio = 0

#     def Iniciar(self):
#         self.GerarNumero()
#         try:
#             while True:
#                 self.PedirValor()
#                 if self.valor > self.aleatorio:
#                     print('alto demais...')

#                 elif self.valor < self.aleatorio:
#                     print('baixo demais...')

#                 else:
#                     print('WTF')
#                     break
#         except:
#             print('erro! digite um numero inteiro.')
#             self.Iniciar()

#     def GerarNumero(self):
#         self.aleatorio = random.randint(1, 100)

#     def PedirValor(self):
#         self.valor = int(input(self.mensagem))


# vai = ChutarNumero()
# vai.Iniciar()

#------------------------------------------------------------------------------------------------------
import random
import PySimpleGUI as sg

class ChutarNumero:
    def __init__(self):
        self.mensagem = 'Tente adivinhar o número...: '
        self.valor = 0
        self.aleatorio = 0
        self.tentar_novamente = True

    def Iniciar(self):
        layout = [
            [sg.Text('Seu chute', size = (40, 0))], #40 altura, 0 largura
            [sg.Input(size=(18,0),  key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(40,10))]
        ]
        #JANELA
        self.janela = sg.Window('Chute o numero.',layout)
        

        self.GerarNumero()
        try:
            while True:
                #receber valores
                self.LerValoresDaTela()
                if self.eventos == sg.WIN_CLOSED:
                    break
                if self.eventos == 'Chutar!':
                    #guardar o valor
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.aleatorio:
                            print('alto demais...')
                            break
                        elif int(self.valor_do_chute) < self.aleatorio:
                            print('baixo demais...')
                            break
                        else:
                            print('WTF')
                            self.tentar_novamente = False
                            break
        except:
            print('erro! digite um numero inteiro.')
            self.Iniciar()

    def GerarNumero(self):
        self.aleatorio = random.randint(1, 100)

    def PedirValor(self):
        self.valor_do_chute = int(input(self.mensagem))

    def LerValoresDaTela(self):
        self.eventos, self.valores = self.janela.read()

vai = ChutarNumero()
vai.Iniciar()