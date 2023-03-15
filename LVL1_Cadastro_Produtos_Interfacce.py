import tkinter as tk
from tkinter import ttk
import datetime as dt

#Função para cadastro
def inserir_codigo():
    descricao = entry_descricao.get() #ler a informação da variavel entry... e armazena em outra.
    tipo = combobox_selecionar_tipo.get() #le a informação da combobox e armazena na variavel 'tipo'.
    quantidade = entry_quantidade_unidade.get()
    data_criacao = dt.datetime.now() #armazenar a data em que o código foi criado.
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M") #formata a aprensentação da data.
    codigo = len(lista_codigos) + 1
    codigo_str = f'COD - {codigo}'
    lista_codigos.append((codigo_str, descricao, tipo, quantidade, data_criacao)) #dois parenteses pois é uma tupla, é imutável. Esta tupla é adicionada a lista de códigos.


lista_tipos = ['caixa', 'sacola', 'papelão']
lista_codigos = []

janela = tk.Tk()
janela.title('cadastro de produtos.')

label_descricao = tk.Label(text='Descrição do Material')
# configurando a posição da label com o método 'grid'
label_descricao.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 4)

entry_descricao = tk.Entry()
entry_descricao.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 4)

label_tipo_unidade = tk.Label(text='Tipo de Unidade do Material')
label_tipo_unidade.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

label_quantidade_unidade = tk.Label(text='Quantidade de Unidade de Material')
label_quantidade_unidade.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

entry_quantidade_unidade = tk.Entry()
entry_quantidade_unidade.grid(row = 4, column = 2, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

botao_criar_codigo = tk.Button(text='Criar Código', command=inserir_codigo) #command chama a função desejada quando o botão é apertado.
botao_criar_codigo.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 4)

janela.mainloop()

print(lista_codigos)
