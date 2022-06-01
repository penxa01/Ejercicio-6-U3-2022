import os
from ClaseListaEnlazada import Lista
from ClaseAparatos import aparato
from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from ClaseLavaropa import Lavarropa
from ObjectEncoder import ObjetcEncoder
from InterfazLista import ILista

class menu:
    __op = None
    __manejador = None
    __ObjEncoder = None

    def __init__(self,op = 0):
        self.__op = op 
        self.__ObjEncoder = ObjetcEncoder()
    
    def setLista(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "aparatoselectronicos.json")
        diccionario = self.__ObjEncoder.leerJSONArchivo(Archivo)
        NuevaLista = self.__ObjEncoder.decodificarDiccionario(diccionario)
        self.__manejador = NuevaLista
    
    def guardarLista(self):
        diccionario = self.__manejador.aJson()
        self.__ObjEncoder.guardarJSONArchivo(diccionario,"aparatoselectronicos.json")
    
    def opciones(self):
        continuar = True

        while continuar:
            self.mostrarOpciones()
            self.__op = int(input("Ingrese opcion deseada\n"))
            os.system("cls")

            if (self.__op == 1):
                self.op1()
            elif(self.__op == 2):
                self.op2()
            elif(self.__op == 3):
                self.op3()
            elif(self.__op == 4):
                self.op4()
            elif(self.__op == 5):
                self.op5()
            elif(self.__op == 6):
                self.op6()
            elif(self.__op == 7):
                continuar = not continuar
                print("Muchas Gracias")
                self.guardarLista()
    
    def op1(self):
        print("Opcion sin terminar")
    def op2(self):
        print("Opcion sin terminar")
    def op3(self):
        print("Opcion sin terminar")
    def op4(self):
        print("Opcion sin terminar")
    def op5(self):
        print("Opcion sin terminar")
    def op6(self):
        print("Opcion sin terminar")
        
    def mostrarOpciones(self):
        print("MENU".center(30,"-"))
        print("[1] Insertar un elemento en una posicion determinada")
        print("[2] Agregar un aparato a la coleccion")
        print("[3] Dada la poscicion de la lista, mostrar el tipo de objeto que se encuentra en la posicion")
        print("[4] Mostrar la cantidad de cada aparato de marca Phillips que haya en la coleccion")
        print("[5] Mostrar todos los lavarropas que tienen carga superior")
        print("[6] Mostrar todos los aparatos que la empresa tiene a la venta(Marca,Pais de fabricacion e importe)")
        print("[7] Para guardar el archivo y SALIR del menu")
    
