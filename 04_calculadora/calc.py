import ttkbootstrap as ttk
from tkinter import messagebox


class Calc:
    def __init__(self):
        pass

    

        




        self.janela = ttk.Window(themename = "minty",
                            title="CuidaBem IMC")
        self.janela.geometry("800x600+100+50")
        self.janela.resizable(False,
                        False)
        self.janela.iconbitmap("04_calculadora/calculator-pink-clipart.ico")

        self.etiqueta = ttk.Label(self.janela,
                            text="cuidabem.com")
        self.etiqueta.pack()


        self.pergunta = ttk.Label(self.janela, 
                            text= "Calcule seu IMC",
                            font= "Arial",
                            style= "info")
        self.pergunta.place(x=340,
                    y=70)

        self.entrada1 = ttk.Label(self.janela,
                            text= "Peso(kg)")
        self.entrada1.place(x=370,
                    y=100)
        self.entrada2 = ttk.Label(self.janela,
                            text="Altura(cm)2")
        self.entrada2.place(x= 360,
                    y= 200 )

        self.e1 = ttk.Entry(self.janela)
        self.e1.place(x=330,
                y= 140)
        self.e2 = ttk.Entry(self.janela)
        self.e2.place(x=330,
                y=240)

        self.botao = ttk.Button(self.janela,
                        text="Calcular",
                        style="outline button",
                        command=self.resultados1)
        self.botao.place(x=361,
                    y=280)

        self.resultado = ttk.Label(self.janela,
                            text="")
        self.resultado.place(x=310,
                        y=320)
    def resultados1(self):

        try:
            peso = float(self.e1.get())
            altura = float(self.e2.get())
            imc = peso / (altura ** 2)
        except ValueError:
            messagebox.showerror("Erro", "Porfavor, insira valores válidos")
        except ZeroDivisionError:
            messagebox.showerror("Erro", "O valor não pode ser 0")
        except:
            messagebox.showerror("Erro", "Erro")
 

  
        

        if imc < 18.5:
            status = "Abaixo do peso"
        elif imc < 24.9:
            status = "Peso Normal"
        elif imc < 29.9:
            status = "Pré Obesidade"
        elif imc < 34.9:
            status = "Obesidade, Grau 1"
        elif imc < 39.9:
            status = "Obesidade, Grau 2"
        else:
            status = "Obesidade Grave"
        
        
        self.resultado.config(text=f"Seu IMC é {imc:.2f} ({status})")



        
    
    def run(self):
        self.janela.mainloop()
    

if __name__ == "__main__":
    calc = Calc()
    calc.janela.mainloop()
    