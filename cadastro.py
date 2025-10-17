import ttkbootstrap as ttk
from tkinter import messagebox

class Cadastro:
    def __init__(self):
        

        self.janela = ttk.Window(title="Cadastro", themename="minty")
        self.janela.geometry("800x600")
        self.janela.resizable(False,
                              False)
        
        frame = ttk.Frame()
        frame.pack()

        ttk.Label(self.janela,
                  text="Cadastro",
                  font= ('Arial', 20)).pack(pady=(60,20))
        
        self.nome = ttk.Label(self.janela,
                              text="Digite seu nome completo:")
        self.nome.pack(pady=5)
        self.logi = ttk.Entry(self.janela)
        self.logi.pack(pady=(0,20))

        
        self.usu = ttk.Label(self.janela,
                             text="Digite seu usuário")
        
        self.usu.pack(pady=5)
        self.login = ttk.Entry(self.janela)
        self.login.pack(pady=(0,20))

        self.sen = ttk.Label(self.janela,
                             text="Digite sua senha:")
        self.sen.pack(pady=(0,20))

        self.senha = ttk.Entry(self.janela, show="*")
        self.senha.pack(pady=(0,20))


















def run(self):
        self.cadastro.mainloop()



if __name__ == "__main__":
    cadastro = Cadastro(ttk.Window())
    cadastro.run()