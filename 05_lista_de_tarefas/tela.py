import ttkbootstrap as ttk
from tkinter import messagebox


class Login:
    def __init__(self):
        

        self.janela = ttk.Window(title="Login", themename="minty")
        self.janela.geometry("800x600")
        self.janela.resizable(False,
                              False)
        
        frame = ttk.Frame()
        frame.pack()

        ttk.Label(self.janela,
                  text="Login",
                  font= ('Arial', 20)).pack(pady=(60,20))
        
        self.nome = ttk.Label(self.janela,
                              text="Nome:")
        self.nome.pack(pady=5)
        self.logi = ttk.Entry(self.janela)
        self.logi.pack(pady=(0,20))

        
        self.usu = ttk.Label(self.janela,
                             text="Usuário:")
        
        self.usu.pack(pady=5)
        self.login = ttk.Entry(self.janela)
        self.login.pack(pady=(0,20))



        self.sen = ttk.Label(self.janela,
                             text="Senha")
        self.sen.pack(pady=(0,20))

        self.senha = ttk.Entry(self.janela, show="*")
        self.senha.pack(pady=(0,20))


        botoes = ttk.Frame()
        botoes.pack()

        ttk.Button(botoes, text="LOGIN", style="outline button", command=self.logar).pack(side="left", padx="10")
        ttk.Button(botoes, text="SAIR", style="outline button", command=self.sair).pack(side="right", padx="10")

    def logar(self):
        login = self.login.get()
        nome = self.nome.get()
        senha = self.senha.get()


        if login == "mari" and senha == "1107" and nome == "mariana":
            messagebox.showinfo("Bem vindo!", "Informações Corretas!")
        
        else:
            messagebox.askretrycancel("Erro", "Informações Incorretas!")
        
    def sair(self):
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja sair?")
        if resposta:
            self.janela.destroy()




    def run(self):
        self.janela.mainloop()
    

if __name__ == "__main__":
    login = Login()
    login.janela.mainloop()