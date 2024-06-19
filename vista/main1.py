import sys
import random
sys.path.append('../')
from controller.historialComandoDaoControl import HistorialComandoDaoControl
from controller.tda.linked.linkedList import LinkedList
import time

lista = LinkedList()
        
for i in range(20000):
    lista.add(random.randint(0, 10000))

inicio = time.time()
lista_ordenada = lista.ordenamiento_numeros("Merge",type=2)
fin = time.time()

inicio2 = time.time()
lista_ordenada2 = lista.ordenamiento_numeros("Quick",type=1)
fin2 = time.time()

inicio3 = time.time()
lista_ordenada3 = lista.ordenamiento_numeros("Shell",type=1)
fin3 = time.time()

print("tiempo merge: ", fin-inicio)
print("tiempo quick: ", fin2-inicio2)
print("tiempo shell: ", fin3-inicio3)