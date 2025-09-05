import ttkbootstrap  as ttk
from bot_gemini import Bot

class Chat():
    def __init__(self):
        #criando janela
        #para ver os temas: python -m ttkbootstrap
        #tema e nome da janela
        self.janela = ttk.Window(themename="morph",
                            title= "Sra. Isadora Leclair")
        #definir tamanho da tela
        self.janela.geometry("800x600")
        
        #definir para nao conseguir mudar o tamanho da janela 
        self.janela.resizable(False, False)

        #etiqueta para colocar o nome do site em cima de tudo
        self.janela_etiqueta= ttk.Label(self.janela,
                             text= "leclairstudio.com")
        self.janela_etiqueta.pack()

        #parte para colocar o texto
        self.janela_nome= ttk(self.janela,
                            text="Sra. Isadora Leclair responde:",
                            style= "info")
        self.janela_nome.pack(padx=20, pady=10)

        #entry para colocar a parte para a pessoa digitar
        self.janela_entrada = ttk.Entry(self.janela)
        self.janela_entrada.pack(padx=30, pady=10)

        #button para criar um botão 
        self.janela_botao = ttk.Button(self.janela,
                                 text= "responder",
                                 style="outline button",
                                 command=self.responder)
        self.janela_botao.pack(padx= 30, pady=5)

        self.label_resposta = ttk.Label(self.janela,
                                   text="",
                                   style= "success")
        self.label_resposta.pack(pady=(20,0))

        self.st = ttk.ScrolledText(self.janela,
                                   height=10,
                                   wrap="word")
        
        self.st.pack(pady=10, padx=10, fill="word")
        

        self.robo = Bot()

    def responder(self):
        pergunta = self.janela_entrada.get()
        resposta = self.robo.enviar_mensagem(pergunta)
        self.label_resposta.config(text=resposta)

        
        self.st.delete("1.0", ttk.END)
        self.st.insert("1.0", resposta)


    def run(self):
        self.janela.mainloop()




if __name__ == "__main__":
    chat = Chat()
    chat.janela.mainloop()