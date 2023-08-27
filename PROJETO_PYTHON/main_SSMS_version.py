import tkinter as tk
from tkinter import ttk
import datetime as dt
from modulos import *
from tkinter import messagebox

lista_situacao = ['pendente','concluido']




def pegar_dados():
    tema = entry_tema.get()
    topico = entry_topico.get()
    situacao = situacao_seletor.get()
    data_criacao = str(dt.datetime.now())  
    enviar_sql(tema, topico, situacao, data_criacao[:19])
    popup()
    limpar()

def limpar():
    entry_tema.delete(0, 100)
    entry_topico.delete(0, 100)
    situacao_seletor.delete(0, 100)

def popup():
        messagebox.showinfo('Aviso','informação registrada com sucesso!')


windows = tk.Tk() #janela
windows.title('Cadastro de topicos para estudo') #titulo da janela

#tema--------------------------------------------------
label_tema = tk.Label(text='Tema') #rotulo
label_tema.grid(row=1, column= 0 , padx= 10, pady= 2, sticky='nswe', columnspan= 4) 

entry_tema = tk.Entry() 
entry_tema.grid(row=2, column= 0 , padx= 10, pady= 2, sticky='nswe', columnspan= 4)

#topico-------------------------------------------------
label_topico = tk.Label(text='topico') #rotulo
label_topico.grid(row=1, column= 5 , padx= 10, pady= 2, sticky='nswe', columnspan= 4) 

entry_topico = tk.Entry() 
entry_topico.grid(row=2, column= 5 , padx= 10, pady= 2, sticky='nswe', columnspan= 4)

#situação------------------------------------------------
label_situacao = tk.Label(text='situacao') 
label_situacao.grid(row=1, column= 10 , padx= 10, pady= 2, sticky='nswe', columnspan= 4) 

situacao_seletor = ttk.Combobox(values=lista_situacao,)
situacao_seletor.grid(row=2, column= 10 , padx= 10, pady= 2, sticky='nswe', columnspan= 4)

#botão ok------------------------------------------------------
botao_ok = tk.Button(text='Enviar dados', command=pegar_dados)
botao_ok.grid(row=3, column= 6 , padx= 10, pady= 20, sticky='nswe', columnspan= 6)

#botão limpar------------------------------------------------------
botao_limpar = tk.Button(text='Limpar', command=limpar)
botao_limpar.grid(row=3, column= 1 , padx= 10, pady= 20, sticky='nswe', columnspan= 6)

windows.mainloop()
