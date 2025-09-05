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
        self.janela_nome= ttk.Label(self.janela,
                            text="Sra. Isadora Leclair responde:",
                            font= "Arial",
                            style= "info")
        self.janela_nome.pack(padx=20, pady=10)

        #entry para colocar a parte para a pessoa digitar
        self.janela_entrada = ttk.Entry(self.janela)
        self.janela_entrada.pack(padx=30, pady=10)

        #button para criar um botão 
        self.janela_botao = ttk.Button(self.janela,
                                 text= "responder",
                                 style="outline button")
        self.janela_botao.pack(padx= 30, pady=5)

        label_resposta = ttk.Label(self.janela,
                                   text="resposta",
                                   style= "success")
        label_resposta.pack(pady=(20,0))

def responder(self):
    pergunta = self.janela_entrada.get()
    robo = Bot()
        

def run(self):
    self.janela.mainloop()




if __name__ == "__main__":
    chat = Chat()
    chat.janela.mainloop()