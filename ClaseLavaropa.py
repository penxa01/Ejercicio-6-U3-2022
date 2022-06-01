from ClaseAparatos import aparato
import json

class Lavarropa(aparato):
    __capacidad = None
    __velocidad = None
    __cantProgramas = None
    __tipoCarga =None

    def __init__(self,marca,modelo,color,pais,precio,capacidad:int,velocidad:int,cantProgramas:int,tipoCarga:str):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidad = capacidad
        self.__velocidad = velocidad
        self.__cantProgramas = cantProgramas
        self.__tipoCarga = tipoCarga

    def __str__(self):
        cadena = ""
        cadena += super().__str__() + ("Capacidad de lavado:{}\nVelocidad de centrifugado:{}\nCantidad de programas:{}\nTipo de carga:{}".format(self.__capacidad,self.__velCentrifugado,self.__cantProg,self.__tipoCarga))
        return cadena

    def getCapacidad(self)->int:
        return self.__capacidad
    
    def getVelocidad(self):
        return self.__velCentrifugado

    def getCantidad(self):
        return self.__cantProg
    
    def getTipoCarga(self):
        return self.__tipoCarga
    
    def getImporte(self):
        importe = self.__precio

        if(self.__capacidad <= 5):
            importe += importe * 0.01
        else:
            importe += importe * 0.03
        return importe

    def toJSON(self):
        diccionarioLavarropa = dict(__class__ = self.__class__.__name__, 
        __atributos__ = dict(
            marca = self.__marca,
            modelo = self.__modelo,
            color = self.__color,
            pais = self.__pais,
            precio = self.__precio,
            capcidad = self.__capacidad,
            velocidadCentr = self.__velCentrifugado,
            cantProg = self.__cantProg,
            tipoCarga = self.__tipoCarga)
        )
        return diccionarioLavarropa