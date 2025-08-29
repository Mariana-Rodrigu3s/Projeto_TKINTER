import ttkbootstrap as tk

#def para o botao clicar
def acao_do_botao():
    print("botao clicado")


#def para a caixa de adicionar nome 
def mostrar_nome():
    nome_digitado = campo_nome.get()
    label_resultado.config(text= f"Olá {nome_digitado}")

janela = tk.Window(themename= "superhero")

menu = 



#Colocar Titulo
janela.title("Janela")
label_etiqueta = tk.Label(janela,
                          text="HelloWorld.org")
label_etiqueta.pack()


#Essa é a variavel para a caixa do "Digite seu nome"
label_nome = tk.Label(janela, 
                      text="Digite seu nome:")
label_nome.place(x=350,
                 y=300)


#cria a parte para voce digitar seu nome
campo_nome = tk.Entry(janela)
campo_nome.place(x=331,
                 y=320)


#cria o botao de enviar seu nome
botao_enviar = tk.Button(janela, 
                         text="enviar", 
                         command=mostrar_nome)
botao_enviar.place(x=369,
                   y=359)


#cria a parte em que vai aparecer seu nome
label_resultado = tk.Label(janela, 
                           text="",
                           font=("Cambria", 16))
label_resultado.place(x=342,
                      y=398)


#caixa de texto
label_titulo = tk.Label(janela, 
                        text="Bem Vindo", 
                        font=("Arial", 16))
label_titulo.place(x=342, 
                   y=260)



#Colocar Cores


#Definir o tamanho da janela e a posição inicial 
janela.geometry("800x600+100+50")

#Colocar Icone na Janela 
janela.iconbitmap("01_Hello_World/happy-face.ico")

#Impede que o usuário redimensione a tela 
janela.resizable(False,
                 False)










janela.mainloop()