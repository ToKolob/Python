import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

i = 0
def iniciar (i):
  print('iniciar' + str(i))
  i += 1
  
janela = tk.Tk()
janela.geometry('300x300')
janela.title('Pomodoro')
texto_orientação= tk.Label(janela, text='Pomodoro Schedule')
texto_orientação.grid(row=0, column=0, padx=10, pady=10)

texto_orientação2= tk.Label(janela, text='Iniciar')
texto_orientação2.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(janela, text='Iniciar', command=iniciar(i))
botao.grid(row=2, column=0, padx=10, pady=10)


janela.mainloop()