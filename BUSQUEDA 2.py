class Busqueda:
    def __init__(self,listas=None):
        self.__lista=listas
    
    
    @property
    def lista(self): # getPropery() son los que retornan el valor de un atributo privado
        if self.__lista != None:
            return self.__lista
        else:
            print("Lista vacia")
    
    
    @lista.setter
    def lista(self,value): # setProperty() cambia el valor de un atributo privado
        self.__lista=value
        
        
    #busca un dato en la lista
    def buquedaLineal(self,buscado):
        lon = len(self.__lista)
        enc = False
        pos = 0
        # recorre la lista hasta encontrar el dato buscado o pos sea igual a la longitud de la lista
        # indica que el dato no fue encontrado
        while pos < lon and enc==False:
            if self.__lista[pos] ["nombre"] == buscado: enc=True
            else: pos +=1
        if enc: return pos
        else: return -1
        
    
    
    
    
    
    def ordernar(self,orden):
      if orden == "asc":  
        for pos in range(0,len(self.__lista)):
            for sig in range(pos+1,len(self.__lista)):
                if self.__lista[pos]["nombre"] > self.__lista[sig] ["nombre"]:
                    aux = self.__lista[pos]
                    self.__lista[pos]=self.__lista[sig]
                    self.__lista[sig]=aux
      else:
        for pos in range(0,len(self.__lista)):
            for sig in range(pos+1,len(self.__lista)):
                if self.__lista[pos]["nombre"] < self.__lista[sig] ["nombre"]:
                    aux = self.__lista[pos]
                    self.__lista[pos]=self.__lista[sig]
                    self.__lista[sig]=aux      
    
    
    
    
    def ordenarQuickSort():
        pass
    
    
    
    
    
    def busquedaBinaria(self,buscado):
        self.ordernar("asc")
        
        fin = len(self.lista)-1     # guarda la posicion final del aegmento
        inicio = 0                  # guarda la poscion inicial del segmento lista
        enc = False
        # se busca mientras que la posicion incial sea menor que la fila
        while  inicio <= fin and enc==False:
            medio = (inicio+fin)//2
            if self.lista[medio] ["nombre"] == buscado: enc= True
            elif self.lista[medio] ["nombre"] < buscado: inicio = medio+1
            else: fin = medio-1
        
        if enc: return medio
        else: return -1
    
    
    
notas = [
    {"nombre":"Ana","n1":60,"n2":40},
    {"nombre":"Daniel","n1":20,"n2":40},
    {"nombre":"Danny","n1":30,"n2":50},
    {"nombre":"Dayana","n1":40,"n2":50},
    {"nombre":"Erick","n1":50,"n2":40},
    {"nombre":"Romina","n1":55,"n2":40}
]    
    
lista = [2,4,5,7,8,9]
print(lista.index(5))





# print(notas[3])
bus1 = Busqueda(notas)  
pos = bus1.busquedaBinaria("Erick")
if pos >=0: print(bus1.lista[pos])
else: print("No esxiste ese nomnre en la lista")



# print(bus1.buquedaLineal("Erick"))

# bus1.ordernar()
# print(bus1.lista)




  
# bus1 = Busqueda([2,4,6])
# bus1.buquedaLineal("ok") 
# bus1.lista=[1,3,5,8,9,10]
# print("bus1",bus1.lista)

# bus2 = Busqueda(["Ana","Dan","Abdon"])
# bus2.buquedaLineal("aceptar")
# print("bus2",bus2.lista)
