import ttkbootstrap as ttk
import sqlite3
from tkinter import messagebox


class Cadastro:
    def __init__(self, janela_pai):
        

        self.janela = ttk.Toplevel(janela_pai)
        self.janela.geometry("800x600")
        self.janela.resizable(False,
                              False)
        self.janela.iconbitmap("05_lista_de_tarefas/download.ico")
        
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


        self.janela_botao = ttk.Button(self.janela, text="Cadastrar", command=self.inserir, )
        self.janela_botao.pack( padx=20, pady=20)

        self.tabela_usuario()

    def tabela_usuario(self):
        #conecatndo banco de dados
        conexao = sqlite3.connect("./bdlista.sqlite")
        #criar cursor
        cursor = conexao.cursor()
        #executar comando
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuario (
                        nome VARCHAR(80),
                        usuario VARCHAR (20) PRIMARY KEY,
                        senha VARCHAR(20));
                        """)
        #comito a transição
        conexao.commit()
        #encerrar a conexão
        conexao.close()

    def inserir(self):
            
             
            
            try:
                conexao = sqlite3.connect("./bdlista.sqlite")

                cursor = conexao.cursor()

                nome = self.logi.get()
                usuario = self.login.get()
                senha = self.senha.get()

                cursor.execute("""
                            INSERT INTO usuario
                        (nome,
                        usuario,
                        senha)
                    VALUES
                        (?,
                        ?,
                        ?)
                                """,
                                [nome, 
                                usuario,
                                senha]
                            )
                
                conexao.commit()
                

                messagebox.showinfo("Concluído", "Você foi cadastrado com sucesso")
            
            except:
                messagebox.showerror("Erro", "Erro ao cadastrar")

            #finally serve para: independente se der certo ou errado, ele vai executar tal comando
            finally:
                conexao.close()


        


















def run(self):
        self.cadastro.mainloop()



if __name__ == "__main__":
    login = Cadastro("jdkfs")
    login.janela.mainloop()




    