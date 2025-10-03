import ttkbootstrap as ttk
from tkinter import messagebox
from tkinter import Listbox, END
import sqlite3




class Lista:
    def __init__(self):

        self.janela = ttk.Window(title= "Lista de Tarefas", themename= "morph")
        self.janela.geometry("800x600")
        self.janela.resizable(False,False)
        self.janela.iconbitmap("05_lista_de_tarefas/download.ico")

        self.janela = ttk.Label(text= "Lista de Tarefa").pack()
        
        
        frame = ttk.Frame(self.janela)
        frame.pack(fill="x", 
                   padx=20)

        self.tarefa = ttk.Entry(frame)
        self.tarefa.pack(side="left", 
                         expand=True, 
                         fill= "x")

        adicionar = ttk.Button(frame,
                                text= "Adicionar Tarefa", 
                                command=self.adicionar_tarefa)
        adicionar.pack(side="right")
        
        self.list = Listbox(self.janela, 
                       font=("Segoue UI", 12), 
                       height=10)
        self.list.pack(pady=20, 
                  padx=20, 
                  fill="both", 
                  expand= True)


        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack(side="bottom", 
                         padx=20)

        excluir = ttk.Button(frame_botao, 
                             text="Excluir", 
                             style="outline button",
                             command=self.excluir_item)
        excluir.pack(side="left", 
                     padx=20)

        feito = ttk.Button(frame_botao, 
                           text="Feito", 
                           style="outline button",
                           command=self.marcar_concluido)
        feito.pack(side="right", 
                   padx=20)
        

        conexao = sqlite3.connect("05_lista_de_tarefas/bdlista.sqlite")

        

        cursor = conexao.cursor()

        tabela = """
                        CREATE TABLE IF NOT EXISTS tarefa(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       tarefa VARCHAR(200));
                """

        cursor.execute(tabela)

        conexao.commit()

        cursor.close()
        conexao.close()



        def atualizar(self):
            conexao = sqlite3.connect("05_lista_de_tarefas/bdlista.sqlite")
            cursor = conexao.cursor()

            selecionar = """
                        SELECT id, tarefa FROM tarefa;
                        """

            lista = cursor.fetchall()
            cursor.execute(selecionar)

            cursor.close()
            conexao.close()

            for linha in lista:
                self.list.insert("end", linha[1])
        

        


    def adicionar_tarefa(self):
        tarefa = self.tarefa.get()
        self.list.insert(END, 
                         tarefa)
        
        conexao = sqlite3.connect("05_lista_de_tarefas/bdlista.sqlite")
        cursor = conexao.cursor()

        insert = """
                INSERT INTO tarefa(tarefa)
                VALUES(?)
"""



        cursor.execute(insert,[tarefa])

        conexao.commit()

        cursor.close()
        conexao.close()

        
        

    
    def excluir_item(self):
        selecionado = self.list.curselection()

        if selecionado:
            self.list.delete(selecionado)
        
        else:
            messagebox.showerror(message="Selecione um item da lista para excluir!")
            

    def marcar_concluido(self):
        concluido = self.list.curselection()

        if concluido:
            item = self.list.get(concluido)

            novo_item = item + " [✓]"

            self.list.delete(concluido)
            self.list.insert(concluido, novo_item)
    

        else:
            messagebox.showerror(message="Selecione um item para concluir")


    def run(self):
        self.janela.mainloop()
    

if __name__ == "__main__":
    lista = Lista()
    lista.run()
    
    
    