import ttkbootstrap as ttk
from tkinter import messagebox



class Lista:
    def __init__(self):

        self.janela = ttk.Window(title= "Lista de Tarefas", themename= "minty")
        self.janela.geometry("800x600")
        self.janela.resizable(False,
                            False)
        self.janela.iconbitmap("05_lista_de_tarefas/download.ico")

        
        
        
        







    def run(self):
        self.janela.mainloop()
    

if __name__ == "__main__":
    lista = Lista()
    lista.janela.mainloop()