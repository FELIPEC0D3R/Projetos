from tkinter import * # Importando biblioteca do tkinter
from tkinter import filedialog # Importando o módulo filedialog da biblioteca tkinter

root = Tk() # Abrindo a interface do tkinter
root.geometry("600x600") # Ajustando a largura e altura da interface
root.title("Bloco de notas") # Adicionando título na interface
root.config(bg = "lightblue") # Adicionando uma cor de fundo na interface
root.resizable(False, False) # Proibindo o usuário de ajustar o tamanho da interface manualmente

# Criando função para salvar o arquivo de texto com a extensão .txt
def save_file(): 
    open_file= filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()    

# Criando função para abrir arquivos de textos já existentes no computador, ou arquivos de texto que acabaram de serem salvos
def open_file():
    file=filedialog.askopenfile(mode='r', filetype=[('text files', '*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT, content)        

# Criando botão que vai receber a função de salvar arquivo de texto
b1 = Button(root, width='20', height='2', bg= '#fff', text = "save file", command= save_file).place(x=100, y=5)

# Criando botão que vai abrir os arquivos de texto
b2 = Button(root, width='20', height='2', bg= '#fff', text = "open file", command= open_file).place(x=300, y=5)

# Criando campo de texto onde o usuário poderá digitar
entry=Text(root, height='33', width='72', wrap=WORD) # Ajustando a altura e largura do campo de texto

# Ajustando o eixo x e y do campo de texto
entry.place(x=10, y=60)


root.mainloop()  # Deixando a interface visível
