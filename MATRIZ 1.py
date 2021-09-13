import os
class Matriz:
    def __init__(self,nfilas,ncols):
        self.matriz = []
        self.noFilas = nfilas
        self.noCols = ncols
        
    def mostrar(self):
        os.system("cls")
        print("------------------------------------")
        for fila in range(len(self.matriz)):
            #print(self.matriz[fila])
            for col in range(len(self.matriz[fila])):
                print(" [{}] ".format(self.matriz[fila][col]), end=" ")
            print()
        print("-----------------------")
            
    def buscar(self,buscado):

        resp = {}
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col] == buscado:
                    resp["fila"] = fila
                    resp["col"]=col
                    break
            if resp: break
        return resp
    
    def buscarW(self,buscado):

        resp = {}
        fila=0
        enc = False
        while fila < len(self.matriz) and enc==False:
            col=0
            while col < len(self.matriz[fila]) and enc==False:
                if self.matriz[fila][col] == buscado:
                    resp["fila"] = fila
                    resp["col"]=col
                    enc=True
                else: col +=1
            fila +=1
        return resp
            
    def ingresar(self):
        self.matriz = []
        for fila in range(self.noFilas):
            columnas = []
            for col in range(self.noCols):
                valor = input("Fila[{}] Col[{}]".format(fila,col))  
                columnas.append(valor)                  
            self.matriz.append(columnas)
            print(self.matriz)
            
            
numeros = [[11,20,15],[10,25,30],[11,21,31]]

mat = Matriz(numeros)
resp = mat.buscar(225)
if resp:print(resp)
else:print("dato no encontrado")