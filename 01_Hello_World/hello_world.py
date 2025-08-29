import tkinter as tk

#def para o botao clicar
def acao_do_botao():
    print("botao clicado")


#def para a caixa de adicionar nome 
def mostrar_nome():
    nome_digitado = campo_nome.get()
    label_resultado.config(text= f"Olá {nome_digitado}")

janela = tk.Tk()


#Colocar Titulo
janela.title("Janela")


#Essa é a variavel para a caixa do "Digite seu nome"
label_nome = tk.Label(janela, 
                      text="Digite seu nome:")
label_nome.place(x=350,
                 y=300)


#cria a parte para voce digitar seu nome
campo_nome = tk.Entry(janela)
campo_nome.place(x=340,
                 y=320)


#cria o botao de enviar seu nome
botao_enviar = tk.Button(janela, 
                         text="enviar", 
                         command=mostrar_nome)
botao_enviar.place(x=375,
                   y=343)


#cria a parte em que vai aparecer seu nome
label_resultado = tk.Label(janela, text="")
label_resultado.place(x=365,
                      y=378)


#caixa de texto
label_titulo = tk.Label(janela, 
                        text="Oi ne", 
                        font=("Arial", 16))
label_titulo.place(x=370, 
                   y=260)



#Colocar Cores
janela.configure(bg="#FACADA")

#Definir o tamanho da janela e a posição inicial 
janela.geometry("800x600+100+50")

#Colocar Icone na Janela 
janela.iconbitmap("01_Hello_World/happy-face.ico")

#Impede que o usuário redimensione a tela 
janela.resizable(False,
                 False)










janela.mainloop()