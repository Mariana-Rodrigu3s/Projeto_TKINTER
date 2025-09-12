from tkinter import Tk

def somar():
    global resultado
    texto = entrada_de_texto.get()
    numero = int(texto)
    resultado += numero
    print("Resultado: %i"%resultado)

janela = Tk()
resultado = 0

entrada_de_texto = Tk.en(janela,width=10,bg="white",font=("Arial",15))
entrada_de_texto.pack()

botao = Tk.Button(janela,text="Somar",command=somar).pack()
janela.mainloop()