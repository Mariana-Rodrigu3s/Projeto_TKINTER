import ttkbootstrap as ttk
import sqlite3

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


        self.button = ttk.Label(self.janela,
                                text="Cadastrar",
                                style="outline button")
        self.button.pack(pady=(0,20))

        self.criar_tabela()


        def criar_tabela(self):
             #conectando ao banco de dados 
             conexao = sqlite3.connect("./bdlista.sqlite")

             #criar cursor
             cursor = conexao.cursor()


             #executando o comando 

             cursor.execute("""
                            CREATE TABLE IF NOT EXISTS usuario(
                                nome VARCHAR(80), 
                                usuario VARCHAR(20) PRIMARY KEY,
                                senha VARCHAR(20)
                            );
                            """)
             
             #comito a transação
             conexao.commit()

            
            #encerro a conexao
             conexao.close()


        def inserir(self):
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
                            (nome, 
                             usuario,
                             senha))
             
             conexao.commit()
             conexao.close()

        


















def run(self):
        self.cadastro.mainloop()



if __name__ == "__main__":
    login = Cadastro()
    login.janela.mainloop()




    