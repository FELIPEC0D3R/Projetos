import datetime # Importando biblioteca que pega a data e o horário do seu computador
from tkinter import messagebox # Importando biblioteca que exibe mensagens de alerta para o usuário
import pyautogui # Importando biblioteca que automatiza processos
import time # Importando biblioteca que defini um tempo entre uma ação e outra
from tkinter import * # Importando módulos do tkinter

root = Tk() # Abrindo a interface do tkinter
root.title("Print")  # Adicionando título na interface
root.geometry("500x550+690+280")  # Ajustando a largura, altura, posição x e posição y da interface
root.resizable(False, False) # Proibindo o usuário de ajustar o tamanho da interface manualmente
root.config(bg= '#A020F0') # Adicionando uma cor de fundo na interface

# nomeando o arquivo print com sua data de criação e a extensão .png 
nomeArquivo = datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.png') 

# Função que é responsável por esperar 3 segundos para tirar um print da tela após eu clicar no botão
def save():
    # Minimizando a interface para não atrapalhar o print
    root.overrideredirect(False)
    root.iconify()
    root.wm_attributes('-fullscreen', 'True')
    # Aqui começa a parte do print
    time.sleep(3)
    foto = pyautogui.screenshot()
    foto.save('salvar print' + nomeArquivo)
    pyautogui.alert(title = "Sucesso", text = "Print salvo") # Exibe uma mensagem após o print ser salvo
    root.after(1000,root.destroy) # Fechando a interface depois de 1 segundo após ela ter feito oq eu pedi

# Botão que recebe a função "save" para salvar o print
btn = Button(root, text= "Salvar print", width=25, height=5, font = ('Arial'), bg='#4B0082', fg='#F8F8FF', border = 0 ,command= save)
btn.place(x = 130, y=200) # Ajustando posição x e y do botão

root.mainloop()  # Deixando a interface visível
