import email
from tkinter import *
from tkinter import messagebox
import database


app = Tk()
app.title("Tela de Login")
app.config(bg = "#ADD8E6")
app.resizable(False, False)

window_width = 1000
window_height = 550

# Obter as dimensões da tela
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


def Cadastrar():
    app.title("Tela de Cadastro")
    lblTituloLogin.place(x = 5000, y = 5000)
    labelNome.place(x = 50, y = 190)
    campoNome.place(x = 128, y = 195)
    campoNome.delete(0, END)
    lblEmail.place(x = 50, y = 240)
    campoEmail.place(x = 128, y = 245)
    campoEmail.delete(0, END)
    labelSenha.place(x = 50, y = 290)
    campoSenha.place(x = 128, y = 295)
    campoSenha.delete(0, END)
    botaoRegistrar.place(x = 185, y = 450)
    lblTituloCadastro.place(x = 150, y = 100)


def Logar():
    app.title("Tela de Login")
    lblTituloLogin.place(x = 150, y = 100)
    lblEmail.place(x = 50, y = 190)
    campoEmail.place(x = 128, y = 195)
    campoEmail.delete(0, END)
    labelSenha.place(x = 50, y = 290)
    campoSenha.place(x = 128, y = 295)
    campoSenha.delete(0, END)
    labelNome.place(x = 5000, y = 5000)
    campoNome.place(x = 5000, y = 5000)
    campoNome.delete(0, END)
    botaoRegistrar.place(x = 5000, y = 5000)
    lblTituloCadastro.place(x = 5000, y = 5000)

      

# Encontrar o ponto central
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

#  Definir a posição da janela no centro da tela
app.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

frame = Frame(app, bg="#1E90FF", width = 500, height = 550)
frame.place(x= 0, y = 0)

imagem = PhotoImage(file="user.png")
w = Label(app, image=imagem, bg="#1E90FF")
w.imagem = imagem
w.place(x = 120, y = 140)

frame2 = Frame(app, bg="white", width = 500, height = 550)
frame2.place(x= 500, y = 0)

botaoTelaLogin = Button(frame2, text = "LOGAR", bg = "white", fg = "#1E90FF", border = 0, font=("bold 20"), width = 16, command = Logar)
botaoTelaLogin.place(x = 0, y = 0)

botaoTelaCadastro = Button(frame2, text = "CADASTRAR", bg = "white", fg = "#1E90FF", border = 0, font=("bold 20"), width = 15, command = Cadastrar)
botaoTelaCadastro.place(x = 254, y = 0)

lblTituloLogin = Label(frame2, text="Entrar na Conta", fg="#1E90FF", bg="white", font=("bold 20"))
lblTituloLogin.place(x = 150, y = 100)

lblTituloCadastro = Label(frame2, text="Criar uma Conta", fg="#1E90FF", bg="white", font=("bold 20"))
lblTituloCadastro.place(x = 5000, y = 5000)

labelNome = Label(frame2, text = "NOME", font=("bold 15"), fg = "#1E90FF", bg="white")
labelNome.place(x = 5000, y = 5000)

campoNome = Entry(frame2, width= 33, border = 3, font=("bold 12"))
campoNome.place(x = 5000, y = 5000)

lblEmail = Label(frame2, text = "EMAIL", font=("bold 15"), fg = "#1E90FF", bg="white")
lblEmail.place(x = 50, y = 190)

campoEmail = Entry(frame2, width=33, border = 3, font=("bold 12"))
campoEmail.place(x = 128, y = 195)

labelSenha = Label(frame2, text = "SENHA", font=("bold 15"), fg = "#1E90FF", bg="white")
labelSenha.place(x = 50, y = 290)

campoSenha = Entry(frame2, width=33, border = 3, show = "•", font=("bold 12"))
campoSenha.place(x = 128, y = 295)

def mostrar():
    if campoSenha.cget('show') == '•':
        campoSenha.config(show = '')
    else:
        campoSenha.config(show='•')   


mostrarSenha = Checkbutton(frame2, text = "Mostrar Senha", bg = "white", fg= "#1E90FF", font=("bold 12"), command = mostrar)
mostrarSenha.place(x = 190, y  = 380)


def registrarUsuario():
    nome =  campoNome.get()
    email =  campoEmail.get()
    senha = campoSenha.get()

    if(nome == "" or email =="" or senha == ""):
        messagebox.showerror(title="Erro", message="Por favor preencha todos os campos")

    else:    
        database.cursor.execute("""
        INSERT INTO Users(nome, email, senha) VALUES(?, ?, ?)
        """, (nome, email, senha))
        database.conn.commit()
        messagebox.showinfo(title="Parabéns", message= "Conta criada com sucesso")
        
        campoNome.delete(0, END)
        campoEmail.delete(0, END)
        campoSenha.delete(0, END)


def Login():
    email = campoEmail.get()
    senha = campoSenha.get()

    database.cursor.execute("""
    SELECT * FROM Users
    WHERE (email = ? and senha = ?)
    """, (email, senha))

    VerifyLogin = database.cursor.fetchone()
    try:
        if(email == "" or senha == ""):
            messagebox.showerror("Erro", "Por favor preeencha todos os campos")

        elif(email in VerifyLogin and senha in VerifyLogin):
            messagebox.showinfo(title="Sucesso", message="O Login foi efetuado")

            campoNome.delete(0, END)
            campoEmail.delete(0, END)
            campoSenha.delete(0, END)
            app.destroy()

            import Menu


    except:
        messagebox.showerror(title="Acesso Negado", message="O Email ou a Senha informada não foram encontrados")   


botaoEntrar = Button(frame2, text = "ENTRAR", bg = "#1E90FF", fg = "white", border = 0, font=("bold 20"), command = Login)
botaoEntrar.place(x = 185, y = 450)        


botaoRegistrar = Button(frame2, text = "Cadastrar", bg = "#1E90FF", fg = "white", border = 0, font=("bold 20"), command= registrarUsuario)
botaoRegistrar.place(x = 5000, y = 5000)



app.mainloop()
