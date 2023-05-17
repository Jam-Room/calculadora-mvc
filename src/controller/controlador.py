class CalculadoraControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.controlador = self

    def sumar(self, num1, num2):
        self.modelo.sumar(num1, num2)
        resultado = self.modelo.obtener_resultado()
        self.vista.mostrar_resultado(resultado)

    def restar(self, num1, num2):
        self.modelo.restar(num1, num2)
        resultado = self.modelo.obtener_resultado()
        self.vista.mostrar_resultado(resultado)

    def multiplicar(self, num1, num2):
        self.modelo.multiplicar(num1, num2)
        resultado = self.modelo.obtener_resultado()
        self.vista.mostrar_resultado(resultado)

    def dividir(self, num1, num2):
        self.modelo.dividir(num1, num2)
        resultado = self.modelo.obtener_resultado()
        self.vista.mostrar_resultado(resultado)

    def reset(self):
        self.modelo.resultado = 0
        self.vista.reset()


    def iniciar(self):
        self.vista.iniciar()
