from Registro import PlanAhorro
from manejador import controlador
import csv
if __name__ == '__main__':
    lista = controlador()
    #lista = []
    lista.leerarchivo() 
    print('1.Cambiar valor')
    print('2.Mostrar vehiculos con cuota inferior a la indicada')
    print('3.Mostrar la cantidad paga para licitar')
    print('4.Cambiar cantidad de cuotas pagas')
    opc = int(input("Ingrese opcion"))
    while opc !=4:
        if opc == 1:
            lista.Actualizar()
        elif opc == 2:
            cuota=int(input("Ingrese un valor de cuota:"))
            lista.valorcuota(cuota)
        elif opc == 3:
            codigo = int(input("Ingrese codigo de auto para ver la cantidad paga y licitar"))
            print(lista.licitacion(codigo))
        elif opc == 3:
            print('No se realizo el cambio de cuotas pagas ya que es variable de clase')
            
        print('1.Cambiar valor')
        print('2.Mostrar vehiculos con cuota inferior a la indicada')
        print('3.Mostrar la cantidad paga para licitar')
        print('4.Cambiar cantidad de cuotas pagas')
        opc = int(input("Ingrese opcion"))