
from traceback import print_tb
from nodo import Nodo


class ListaCircularDEnlazada():

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
            self.__unir_nodos

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
            self.__unir_nodos()

    def buscar(self, dato):
        aux = self.primero

        while(aux != None):
            if(aux.dato == dato):
                an = aux.anterior.dato

                print("El valor anterior es: ", an)
                print("---------------------------------")
                print("El valor actual es:", aux.dato)
                au = aux.siguiente.dato
                print("---------------------------------")
                print("El valor  siguiente es:", au)

                return

            aux = aux.siguiente

        print("No encontro el valor")

    def __unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorrer_inicio_fin(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrer_fin_inicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break
