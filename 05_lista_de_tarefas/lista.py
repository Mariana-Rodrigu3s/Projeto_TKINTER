import ttkbootstrap as ttk
from tkinter import messagebox
from tkinter import Listbox



class Lista:
    def __init__(self):

        self.janela = ttk.Window(title= "Lista de Tarefas", themename= "minty")
        self.janela.geometry("800x600")
        self.janela.resizable(False,False)
        self.janela.iconbitmap("05_lista_de_tarefas/download.ico")

        self.janela = ttk.Label(text= "Lista de Tarefa").pack()
        
        
        frame = ttk.Frame(self.janela)
        frame.pack()

        self.tarefa = ttk.Entry(frame)
        self.tarefa.pack(side="left", expand=True, fill= "x")

        adicionar = ttk.Button(frame, text= "Adicionar Tarefa")
        adicionar.pack(side="right")
        
        list = Listbox(self.janela, font=("Segoue UI", 12), height=10)
        list.pack(pady=20, padx=20, fill="both", expand= True)


        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack(side="bottom")

        excluir = ttk.Button(frame_botao, text="Excluir")
        excluir.pack(side="right")

        feito = ttk.Button(frame_botao, text="Feito")
        feito.pack(side="left")


    
    



    def run(self):
        self.janela.mainloop()
    

if __name__ == "__main__":
    lista = Lista()
    lista.janela.mainloop()