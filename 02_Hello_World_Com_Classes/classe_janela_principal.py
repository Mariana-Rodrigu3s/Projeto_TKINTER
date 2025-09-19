import ttkbootstrap as tk


class Janela_Principal:
    """Janela"""

    def __init__(self):
        pass

        
        janela = tk.Window(themename= "superhero")
        
        #Definir o tamanho da janela e a posição inicial 
        self.janela.geometry("800x600+100+50")
        
        #Colocar Icone na Janela 
        self.janela.iconbitmap("01_Hello_World/happy-face.ico")

        #Impede que o usuário redimensione a tela 
        self.janela.resizable(False,
                        False)
        self.janela.state('zoomed')





#Colocar Titulo
        janela.title("Janela")
        self.label_etiqueta = tk.Label(janela,
                                text="HelloWorld.org")
        self.label_etiqueta.pack()


        #Essa é a variavel para a caixa do "Digite seu nome"
        self.label_nome = tk.Label(janela, 
                            text="Digite seu nome:")
        self.label_nome.place(x=350,
                        y=300)


        #cria a parte para voce digitar seu nome
        self.campo_nome = tk.Entry(janela)
        self.campo_nome.place(x=331,
                        y=320)


        #cria o botao de enviar seu nome
        self.botao_enviar = tk.Button(janela, 
                                text="enviar", 
                                command=self.mostrar_nome)
        self.botao_enviar.place(x=369,
                        y=359)


        #cria a parte em que vai aparecer seu nome
        self.label_resultado = tk.Label(janela, 
                                text="",
                                font=("Cambria", 16))
        self.label_resultado.place(x=342,
                            y=398)


        #caixa de texto
        self.label_titulo = tk.Label(janela, 
                                text="Bem Vindo", 
                                font=("Arial", 16))
        self.label_titulo.place(x=342, 
                        y=260)

        
     
        
    def run(self):
        self.janela.mainloop()

        #def para o botao clicar
    def acao_do_botao(self):
            print("botao clicado")


        #def para a caixa de adicionar nome 
    def mostrar_nome(self):
        nome_digitado = self.campo_nome.get()
        self.label_resultado.config(text= f"Olá {nome_digitado}")










