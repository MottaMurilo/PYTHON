from tkinter import *
from tkinter import ttk

cor0 = '#ffffff'    #branco
cor1 = '#444466'    #preto
cor2 = '#4065a1'    #azul

janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg='white')


frame_cima= Frame(janela, width=295, height=50, background=cor0, pady=0, padx=0, relief= 'flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=180, background=cor0, pady=0, padx=0, relief= 'flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold '), bg=cor0, fg=cor1)
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1  '), bg=cor2, fg=cor1)
app_linha.place(x=0, y=35)

def calcular():

    peso = float(e_peso.get())
    altura = float(l_altura.get())
    
    imc= peso / altura**2

    resultado = imc 

    if resultado < 18.5:
         l_resultado_texto['text'] = "Seu IMC é: Abaixo do peso"
    elif resultado >= 18.5 and resultado < 25:
         l_resultado_texto['text'] = "Seu IMC é: Normal"
    elif resultado >= 25 and resultado < 30:
         l_resultado_texto['text'] = "Seu IMC é: Sobrepeso"
    else:
        l_resultado_texto['text'] = "Seu IMC é: Obesidade"
