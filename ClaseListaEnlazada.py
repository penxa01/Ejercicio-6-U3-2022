from ClaseNodo import nodo
from ClaseAparatos import aparato
from zope.interface import Interface
from zope.interface import implementer
from InterfazLista import ILista

@implementer(ILista)
class Lista:
    __comienzo = None

    def __init__(self):
        self.__comienzo = None
        self.__actual =  None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    
    def agregarAparato(self,aparato):
        NuevoNodo = nodo(aparato)
        NuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = NuevoNodo
        self.__actual = NuevoNodo
        self.__tope += 1
    
    def getLongitud(self):
        return self.__tope
    
    def insertarAparato(self,aparato,indice):
        NodoAInsertar = nodo(aparato)
        i = 0
        self.__actual = self.__comienzo
       
        if(indice == 1):
            self.agregarAparato(NodoAInsertar)
        
        while((i < indice-1) and (self.__actual.getSiguiente() is not None)):
            self.__actual = self.__comienzo.getSiguiente()
            i+=1
        if self.__actual.getSiguiente() == None:
            print("Fuera de indice")
        else:
            NodoAInsertar.setSiguiente(self.__actual.getSiguiente())
            self.__actual.setSiguiente(NodoAInsertar)
        
    def mostrarAparato(self,posicionBuscada):
        i = 0
        self.__actual = self.__comienzo
        if (posicionBuscada == 1):
            aparatoBuscado = self.__actual.getDato()
        
        while i < posicionBuscada and self.__actual.getSiguiente != None:
            i += 1
            self.__actual =self.__comienzo.getSiguiente()
        
        if i< posicionBuscada or i > posicionBuscada:
            raise(IndexError("Fuera de indice"))
        
        aparatoBuscado = self.__actual.getDato()
        return aparatoBuscado


    def aJson(self):
        diccionarioLista = dict(
            __class__ = self.__class__.__name__,
            aparatos =[nuevoAparato.toJson() for nuevoAparato in self]
        )
        return diccionarioLista

           
        
        


