import ttkbootstrap as ttk
from tkinter import messagebox
from lista import Lista
from cadastro import Cadastro
import sqlite3

import sqlite3

class Login:
    def __init__(self, janela_pai):
        
        self.janela_pai = janela_pai
        


    #login : entry()
    #senha : entry()


        self.janela = ttk.Toplevel(janela_pai)
        self.janela.geometry("800x600")
        self.janela.resizable(False,
                              False)
        self.janela.iconbitmap("05_lista_de_tarefas/pinkiepie.ico")
        
        
        
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

        
        self.frame_botao = ttk.Frame(self.janela)
        self.frame_botao.pack()


        ttk.Button(self.frame_botao,
                   text="LOGIN",
                   style="outline button",
                   command=self.logar).pack(side="left",padx=10)
        ttk.Button(self.frame_botao,
                   text="SAIR",
                   style="outline button",
                   command=self.sair).pack(side="right",padx=10)
        
        ttk.Button(self.janela,
                   text="CADASTRAR",
                   style = "outline button",
                   command=self.cadastrar).pack(padx=15, pady=10)


        

    def run(self):
        self.janela.mainloop()   

    def cadastrar(self):
         Cadastro(self.janela)
    
    
    def sair(self):
         resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja sair?")
         if resposta == True:
              exit()  

        #Def para validar a senha e ver se está correta ou não 
    def logar(self):
         login = self.login.get()
         senha = self.senha.get()

         conexao = sqlite3.connect("./bdlista.sqlite")

         cursor = conexao.cursor()

         cursor.execute(
              """
              SELECT nome, usuario FROM usuario
              WHERE usuario = ? AND senha = ?;

              """,
              [login, senha]
         )

         resultado = cursor.fetchone()

         conexao.close()



         if resultado:
              messagebox.showinfo("Login e Senha Corretos!", message=f"Bem vindo, {resultado[0]}!!")
              self.janela.destroy()
              
              

         else: 
              messagebox.askretrycancel("Erro","Login e Senha incorretos, tente novamente!")
         
         #Def para perguntar se realmente quer sair da janela 
    


    
    


    

        
    






    




if __name__ == "__main__":
        login = Login("jajs")
        login.janela.mainloop()