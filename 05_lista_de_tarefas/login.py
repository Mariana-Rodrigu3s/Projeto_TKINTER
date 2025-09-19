import ttkbootstrap as ttk
from tkinter import messagebox
from lista import Lista

class Login:
    def __init__(self):
        


    #login : entry()
    #senha : entry()


        self.janela = ttk.Window(title="Login", themename= "minty")
        self.janela.geometry("800x600")
        self.janela.resizable(False,
                              False)
        self.janela.iconbitmap("05_lista_de_tarefas/pinkiepie.ico")
        
        frame = ttk.Frame()
        frame.pack()
        
        #Login
        ttk.Label(self.janela,
                        text="Login:",
                        font= ('Arial', 20)).pack(pady=(60,20))
        
        #Entrada do Usuário
        self.usu = ttk.Label(self.janela,
                             text= "Usuário:")
        self.usu.pack(pady=5)
        self.login = ttk.Entry(self.janela)
        self.login.pack(pady=(0,20))
        
        #Entrada da Senha
        self.sen = ttk.Label(self.janela,
                             text= "Senha:")
        self.sen.pack(pady=(0,20))
        
        self.senha = ttk.Entry(self.janela, show="*")
        self.senha.pack(pady=(0,20))


        #Botao de logar
        botoes = ttk.Frame()
        botoes.pack()

        ttk.Button(botoes, text="LOGIN", style= "outline button", command=self.logar).pack(side="left", padx=10)
        ttk.Button(botoes, text="SAIR", style= "outline button", command=self.sair).pack(side="right", padx=10)

        

        
        

        #Def para validar a senha e ver se está correta ou não 
    def logar(self):
         login = self.login.get()
         senha = self.senha.get()


         if login == "mariana" and senha == "1107":
              messagebox.showinfo("Bem vindo!", "Login e Senha Corretos!")
              self.janela.destroy()
              tarefa = Lista()
              tarefa.run()
              

         else: 
              messagebox.askretrycancel("Erro","Login e Senha incorretos, tente novamente!")
         
         #Def para perguntar se realmente quer sair da janela 
    def sair(self):
         resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja sair?")
         if resposta:
              self.janela.destroy()
    

        
    






    def run(self):
        self.janela.mainloop()




if __name__ == "__main__":
        login = Login()
        login.janela.mainloop()