import ttkbootstrap as ttk
from tkinter import messagebox

class Login:
    def __init__(self):
        self.janela = ttk.Window(title="Lista de Tarefas")
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)

        # Frame principal para centralizar
        frame = ttk.Frame(self.janela)
        frame.pack(expand=True)  # centraliza na janela

        # Login
        ttk.Label(frame,
                  text="Login:",
                  font=('Arial', 20)).pack(pady=20)

        # Entrada do Usuário
        self.usu = ttk.Label(frame, text="Usuário:")
        self.usu.pack(pady=5)

        self.login = ttk.Entry(frame)
        self.login.pack(pady=5)

        # Entrada da Senha
        self.sen = ttk.Label(frame, text="Senha:")
        self.sen.pack(pady=5)

        self.senha = ttk.Entry(frame, show="*")
        self.senha.pack(pady=5)

        # Botões
        botoes = ttk.Frame(frame)
        botoes.pack(pady=20)

        self.logar = ttk.Button(botoes,
                                text="Logar",
                                style="outline button",
                                command=self.validar)
        self.logar.pack(side="left", padx=10)

        self.sair = ttk.Button(botoes,
                               text="Sair",
                               style="outline button",
                               command=self.janela.destroy)
        self.sair.pack(side="left", padx=10)

    # Validação do login
    def validar(self):
        login = self.login.get()
        senha = self.senha.get()

        if login == "mariana" and senha == "1107":
            messagebox.showinfo("Bem vindo!", "Login e Senha Corretos!")
        else:
            messagebox.showerror("Erro", "Login e Senha incorretos, tente novamente!")

    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    login = Login()
    login.run()
