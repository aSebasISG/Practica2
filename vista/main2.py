import sys
import random
sys.path.append('../')
from controller.historialComandoDaoControl import HistorialComandoDaoControl
from controller.tda.linked.linkedList import LinkedList
import time

lista = LinkedList()
        
for i in range(20000):
    lista.add(random.randint(0, 10000))

lista = lista.ordenamiento_numeros("Shell",type=1)

numero_a_buscar = 8000

inicio = time.time()
lista_ordenada = lista.busqueda_secuencial(numero_a_buscar)
fin = time.time()
print("Tiempo de ejecucion de busqueda secuencial: ", fin-inicio)

inicio = time.time()
lista_ordenada = lista.busquedaLinealBinariaNumeros(lista, numero_a_buscar)
fin = time.time()
print("Tiempo de ejecucion de busqueda Lineal: ", fin-inicio)

