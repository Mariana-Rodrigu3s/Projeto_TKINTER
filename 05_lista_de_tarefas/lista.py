import ttkbootstrap as ttk

from tkinter import Listbox, END



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
                           style="outline button")
        feito.pack(side="right", 
                   padx=20)


    def adicionar_tarefa(self):
        tarefa = self.tarefa.get()
        self.list.insert(END, 
                         tarefa)

    
    def excluir_item(self):
        selecionado = self.list.curselection()

        if selecionado:
            self.list.delete(selecionado)

        



    def run(self):
        self.janela.mainloop()
    

if __name__ == "__main__":
    lista = Lista()
    lista.janela.mainloop()