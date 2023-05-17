from tkinter import *

class CalculadoraVistaTkinter:
    def __init__(self):
        # Configuración de la ventana principal
        self.ventana = Tk()
        self.ventana.title("Calculadora")
        self.ventana.geometry("400x250")
        self.ventana.configure(bg="#333333")

        # Etiqueta para mostrar el resultado
        self.resultado = Label(self.ventana, text="Resultado", background='white', height='1', border='2', highlightbackground='#000')
        self.resultado.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.etiqueta_resultado = Label(self.ventana, bg='#9EF8E8', text='0', width=24, relief='groove',
                                        font='Montserrat 16', justify='right', highlightbackground='#000')
        self.etiqueta_resultado.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Entradas de texto para los números
        self.entrada_num1 = Entry(self.ventana, justify='right', font=("Arial", 16))
        self.entrada_num1.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
        self.entrada_num1.insert(0, "0")  # Valor predeterminado "0"
        self.entrada_num1.config(fg='#CCCCCC')  # Color de texto gris

        self.entrada_num2 = Entry(self.ventana, justify='right', font=("Arial", 16))
        self.entrada_num2.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')
        self.entrada_num2.insert(0, "0")  # Valor predeterminado "0"
        self.entrada_num2.config(fg='#CCCCCC')  # Color de texto gris

        # Vincular eventos de clic a las entradas de texto
        self.entrada_num1.bind("<Button-1>", self.borrar_valor_num1)
        self.entrada_num2.bind("<Button-1>", self.borrar_valor_num2)

        self.entrada_num1.bind("<FocusOut>", self.restaurar_valor_num1)
        self.entrada_num2.bind("<FocusOut>", self.restaurar_valor_num2)

        # Boton de suma
        self.boton_suma = Button(self.ventana, text="+", command=self.sumar, bg='#FF9800', highlightbackground='#000', font=("Arial", 16))
        self.boton_suma.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

        # Boton de resta
        self.boton_resta = Button(self.ventana, text="-", command=self.restar, bg='#FF9800', highlightbackground='#000', font=("Arial", 16))
        self.boton_resta.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

        # Botón de multiplicación
        self.boton_multiplicacion = Button(self.ventana, text="x", command=self.multiplicar, bg='#FF9800', highlightbackground='#000', font=("Arial", 16))
        self.boton_multiplicacion.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

        # Botón de división
        self.boton_division = Button(self.ventana, text="/", command=self.dividir, bg='#FF9800', highlightbackground='#000', font=("Arial", 16))
        self.boton_division.grid(row=3, column=3, padx=10, pady=10, sticky='nsew')

        # Botón para limpiar resultado
        self.boton_reset = Button(self.ventana, text="Reset", command=self.reset, bg='#FF9800', highlightbackground='#000', font=("Arial", 16))
        self.boton_reset.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Configurar el redimensionamiento de los botones
        self.ventana.grid_columnconfigure(0, weight=1, uniform='buttons')
        self.ventana.grid_columnconfigure(1, weight=1, uniform='buttons')
        self.ventana.grid_columnconfigure(2, weight=1, uniform='buttons')
        self.ventana.grid_columnconfigure(3, weight=1, uniform='buttons')
        self.ventana.grid_rowconfigure(3, weight=1)

    # Resto del código sin cambios
    #valores en 0
    def borrar_valor_num1(self, event):
        if self.entrada_num1.get() == "0":
            self.entrada_num1.delete(0, 'end')
            self.entrada_num1.config(fg='black')

    def borrar_valor_num2(self, event):
        if self.entrada_num2.get() == "0":
            self.entrada_num2.delete(0, 'end')
            self.entrada_num2.config(fg='black')

    def restaurar_valor_num1(self, event):
        if self.entrada_num1.get() == "":
            self.entrada_num1.delete(0, 'end')
            self.entrada_num1.insert(0, "0")
            self.entrada_num1.config(fg='#CCCCCC')

    def restaurar_valor_num2(self, event):
        if self.entrada_num2.get() == "":
            self.entrada_num2.delete(0, 'end')
            self.entrada_num2.insert(0, "0")
            self.entrada_num2.config(fg='#CCCCCC')
    #Fin valores en 0



    def sumar(self):
        num1 = float(self.entrada_num1.get())
        num2 = float(self.entrada_num2.get())
        self.controlador.sumar(num1, num2)


    def restar(self):
        num1 = float(self.entrada_num1.get())
        num2 = float(self.entrada_num2.get())
        self.controlador.restar(num1, num2)


    def multiplicar(self):
        num1 = float(self.entrada_num1.get())
        num2 = float(self.entrada_num2.get())
        self.controlador.multiplicar(num1, num2)


    def dividir(self):
        num1 = float(self.entrada_num1.get())
        num2 = float(self.entrada_num2.get())

        if num2 != 0:
            self.controlador.dividir(num1, num2)
        else:
            self.mostrar_resultado("Error: División entre cero")
        # Mostrar error para indicar división entre cero



    def mostrar_resultado(self, resultado):
        if isinstance(resultado, str):  # Verificar si el resultado es una cadena de texto
            self.etiqueta_resultado["text"] = resultado
        elif resultado.is_integer():  # Comprobar si el resultado es un número entero
            self.etiqueta_resultado["text"] = str(int(resultado))
        else:
            self.etiqueta_resultado["text"] = "{:.4f}".format(resultado)


    def reset(self):
        self.etiqueta_resultado["text"] = "0"
        self.entrada_num1.delete(0, 'end')
        self.entrada_num1.insert(0, "0")
        self.entrada_num1.config(fg='#CCCCCC')

        self.entrada_num2.delete(0, 'end')
        self.entrada_num2.insert(0, "0")
        self.entrada_num2.config(fg='#CCCCCC')



    def reset(self):
        self.etiqueta_resultado["text"] = "0"

        if self.entrada_num1.focus_get() == self.entrada_num1:  # Verificar si el cursor está en la casilla entrada_num1
            self.entrada_num1.delete(0, 'end')
            self.entrada_num1.insert(0, "")
            self.entrada_num1.config(fg='black')
        else:
            self.entrada_num1.delete(0, 'end')
            self.entrada_num1.insert(0, "0")
            self.entrada_num1.config(fg='#CCCCCC')

        if self.entrada_num2.focus_get() == self.entrada_num2:  # Verificar si el cursor está en la casilla entrada_num2
            self.entrada_num2.delete(0, 'end')
            self.entrada_num2.insert(0, "")
            self.entrada_num2.config(fg='black')
        else:
            self.entrada_num2.delete(0, 'end')
            self.entrada_num2.insert(0, "0")
            self.entrada_num2.config(fg='#CCCCCC')




    def iniciar(self):
        self.ventana.mainloop()
