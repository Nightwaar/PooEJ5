from Registro import PlanAhorro
import csv
class controlador:
    def __init__(self):
        self.__lista=[]
        return
    def leerarchivo(self):
        archivo = open('plan.csv')
        leer = csv.reader(archivo,delimiter=';')
        for fila in leer:
            self.__lista.append(PlanAhorro(fila[0],fila[1],fila[2],fila[3]))     
    def muestra(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
        return
    def Actualizar(self):
        for plan in self.__lista:
            actu = int(input("Ingrese nuevo valor del plan, ingrese 0 para no actualizar"))
            if actu !=0:
                plan.actualizarplan(actu)
        return
    def valorcuota(self,cuota):
        for valor in self.__lista:
            if valor.calcularcuota() < cuota:
                print(valor)
        return
    def licitacion(self,codigo):   
        for cod in self.__lista:
            print(cod.verif(codigo))
            if cod.verif(codigo) == True:
                return "La cantidad paga es: {}".format(cod.valorlic())
    