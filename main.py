from nodo import Nodo
from lista import ListaCircularDEnlazada

lista = ListaCircularDEnlazada()

lista.agregar_final(2)
lista.agregar_final(7)
lista.agregar_final(5)
lista.agregar_final(11)
lista.agregar_final(4)


lista.recorrer_inicio_fin()

Buscar = int(input("ingrese un numero a buscar en la lista:"))
lista.buscar(Buscar)
