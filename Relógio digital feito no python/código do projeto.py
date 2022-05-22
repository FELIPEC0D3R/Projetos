from tkinter import * # Importando os módulos do tkinter
import tkinter # importando o tkinter
from datetime import datetime # Importando biblioteca que pega a data e o horário do seu computador

root = Tk() # Abrindo a interface
root.title("Relógio Digital") # Adicionando título na interface

cor1 = "black" # Definido cor 1 
cor2 = "green" # Definindo cor 2

root.state("zoomed") # Definindo a interface como tela inteira
root.configure(background=cor1) # Adicionando a "cor1" no fundo da interface

#time = datetime.now() # Verifica que horas são no meu computador
#print(time) # Mostra que horas são no meu computador

"""
time = datetime.now()
hour = time.strftime("%H:%M:%S")
weekday = time.strftime("%A") 
day = time.day
month = time.strftime("%b")
year = time.strftime("%y")
complete_date = time.strftime("%c")
print(hour)
print(weekday)
print(day)
print(month)
print(year)
print(complete_date)

"""

# Criando função que mostrará a hora e a data em tempo real dentro da interface
def clock():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    weekday = time.strftime("%A") 
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%y")
    l1.config(text=hour)
    l1.after(200, clock)
    l2.config(text = weekday + " " + str(day) + "/" + str(month) + "/" + (year))

# Mostrando a hora
l1 = Label(root, font=("ds-digital", 80,), bg = cor1, fg = cor2)
l1.pack()

# Mostrando a data
l2 = Label(root, font=('ds-digital', 20), bg = cor1, fg = cor2)
l2.pack()

clock() # Chamando a função "clock"

mainloop() # Deixando a interface visível
