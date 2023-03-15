import sqlite3
import tkinter as tk

import pandas as pd

# CRIANDO O BANCO DE DADOS
# conexao = sqlite3.connect('clientes.db') #'clientes.db' será o nome do banco.
# mensageiro = conexao.cursor()
# mensageiro.execute(''' CREATE TABLE clientes (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
#     )
# ''')
# conexao.commit()
# conexao.close()
# o arquivo db ja é criado, pode ser visualizado com algum programa de banco de dados como o browser for sqlite.


def cadastrar_cliente():
    # 'clientes.db' será o nome do banco.
    conexao = sqlite3.connect('clientes.db')
    mensageiro = conexao.cursor()
    mensageiro.execute("INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)",
                       {
                           'nome': entry_nome.get(),
                           'sobrenome': entry_sobrenome.get(),
                           'email': entry_email.get(),
                           'telefone': entry_telefone.get()
                       }
                       )  # o ':' é necessário para que a variavel seja temporária. Irá colocar os valores nessas variáriveis temporárias, e depois coloca-las em um dicionário, através do get().
    conexao.commit()
    conexao.close()

    # para apagar o campo digitado após apertar o botão e commitar.
    entry_nome.delete(0, 'end')
    entry_sobrenome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')


def exportar_cliente():
    # 'clientes.db' será o nome do banco.
    conexao = sqlite3.connect('clientes.db')
    mensageiro = conexao.cursor()
    # oid é para não pegar dados repetidos, e sim pelo id cadastrado.
    mensageiro.execute("SELECT *, oid FROM clientes")
    # pega os dados selecionados e armazena em uma variavel.
    clientes_cadastrados = mensageiro.fetchall()
    print(clientes_cadastrados)
    # cria um dataframe a partir dos dados armazenados na variavel.
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=[
                                        'nome', 'sobrenome', 'email', 'telefone', 'id'])
    # exporta para o excell.
    clientes_cadastrados.to_excel('banco_clientes.xlsx')
    conexao.commit()
    conexao.close()


# CRIANDO A JANELA
janela = tk.Tk()
janela.title('ferramenta de cadastro de clientes')

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='Email')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)


entry_nome = tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text='Sobrenome', width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='Email', width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='Telefone', width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)


botao_cadastrar = tk.Button(
    janela, text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10,
                     columnspan=2, ipadx=80)  # ipadx expande no eixo x

botao_exportar = tk.Button(
    janela, text='Exportar base Para Excell', command=exportar_cliente)
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

janela.mainloop()
