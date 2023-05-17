from model.modelo import CalculadoraModelo
from view.vista import CalculadoraVistaTkinter
from controller.controlador import CalculadoraControlador

def main():
    #invocamos los modulos
    model = CalculadoraModelo()
    view = CalculadoraVistaTkinter()
    controller = CalculadoraControlador(model, view)
    # Iniciar la aplicación
    controller.iniciar()

#verifica que la funcion main este ejecutada, sino lo esta la inicia
if __name__ == "__main__":
    main()