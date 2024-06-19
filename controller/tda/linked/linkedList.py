
from controller.exception.LinkedEmpty import LinkedEmpty
from controller.tda.linked.node import Node
from controller.exception.arrayPositionException import ArrayPositionException
from controller.exception.vacioException import VacioException
from controller.tda.linked.merge_sort import MergeSort
from controller.tda.linked.quick_sort import QuickSort
from controller.tda.linked.shell_sort import ShellSort
from numbers import Number

class LinkedList(object):

    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value


    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0
    
    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length = self.__length +1
        else:
            headOdl = self.__head
            node = Node(data, headOdl)
            self.__head = node
            self.__length = self.__length +1

    
    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)
        else:
            node = Node(data)
            self.__last._next = node 
            self.__last = node
            self.__length += 1

    def getNode(self, pos):
        if self.isEmpty:
            raise VacioException("Error, la lista esta vacia")
        elif pos < 0  or pos >= self.__length:
            raise ArrayPositionException("Error, Esta fuera de los limites de la lista ")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length -1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:
            self.__addLast__(data)
        else:
            node_preview = self.getNode(pos-1)
            node_last =  node_preview.__next 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1

    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:
            self.__last._data = data
        else:
            node = self.getNode(pos)
            node._data = data

    @property 
    def toArray(self):
        array = []
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self.__length:
                array.append(node._data)
                cont += 1
                node = node._next
        return array

    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])
            
    def deleteFirst(self):
        if self.isEmpty:
            raise VacioException("Lista Vacia")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self._length == 1:
                self.__last = None
            self._length -= 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise VacioException("Lista Vacia")
        else:
            node = self.__head
            while node._next != self.__last:
                node = node._next
            element = self.__last._data
            node._next = None
            self.__last = node
            self._length -= 1
            return element


    def delete(self, pos):
        if self.isEmpty:
            raise VacioException("Lista Vacia")
        elif pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Posición fuera de los límites de la lista")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == self.__length - 1:
            return self.deleteLast()
        else:
            prev_node = self.getNode(pos - 1)
            node_to_delete = prev_node._next
            prev_node._next = node_to_delete._next
            element = node_to_delete._data
            del node_to_delete
            self._length -= 1
            return element
        
    def list_all(self):
        if self.isEmpty:
            print("La lista está vacía.")
        else:
            current_node = self.__head
            while current_node is not None:
                print(current_node._data)
                current_node = current_node._next

    def arreglo_de_diccionarios(self):
        if self.isEmpty:
            return []
        else:
            array = []
            node = self.__head
            while node is not None:
                array.append(node._data.persona_to_dict())
                node = node._next
            return array
        
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def get(self, pos):
        try:
            if self.isEmpty:
                raise VacioException("Error, la lista esta vacia")
            elif pos < 0  or pos >= self.__length:
                raise ArrayPositionException("Error, Esta fuera de los limites de la lista ")
            elif pos == 0:
                return self.__head._data
            elif pos == (self.__length -1):
                return self.__last._data
            else:
                node = self.__head
                cont = 0
                while cont < pos:
                    cont += 1
                    node = node._next
                return node._data
        except Exception as e:
            print(e)


    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = 'List is Empty'
        else:
            node = self.__head
            while node != None:
                out += str(node._data) + " "
                node = node._next
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node is not None:
            data += str(node._data) + "    "
            node = node._next
        print(f'Lista de datos\n{data}')
    
    def ordenamiento_numeros(self, metodo="Merge", type=1):
        if self.isEmpty <= 1:
            array = self.toArray
            if metodo == "Merge":
                order = MergeSort()
                if type == 1:
                    array = order.ordenamiento_merge_ascendente_numeros(array)
                else:
                    array = order.ordenamiento_merge_descendente_numeros(array)
            elif metodo == "Quick":
                order = QuickSort()
                if type == 1:
                    array = order.ordenamiento_quick_numeros_ascendente(array)
                else:
                    array = order.ordenamiento_quick_numeros_descendente(array)
            elif metodo == "Shell":
                order = ShellSort()
                if type == 1:
                    array = order.ordenamiento_shell_numeros_ascendente(array)
                else:
                    array = order.ordenamiento_shell_numeros_descendente(array)
            else:
                raise ValueError(f"Método de ordenamiento '{metodo}' no válido")
            self.toList(array)
            return self
        return None

    def ordenamiento_atributo(self, metodo="Merge", attribute=None, type=1):
        if self.isEmpty <= 1:
            array = self.toArray
            if attribute is not None:
                if metodo == "Merge":
                    order = MergeSort()
                    if type == 1:
                        array = order.ordenamiento_merge_ascendente_atributo(array, attribute)
                    else:
                        array = order.ordenamiento_merge_descendente_atributo(array, attribute)
                elif metodo == "Quick":
                    order = QuickSort()
                    if type == 1:
                        array = order.ordenamiento_quick_atributo_ascendente(array, attribute)
                    else:
                        array = order.ordenamiento_quick_atributo_descendente(array, attribute)
                elif metodo == "Shell":
                    order = ShellSort()
                    if type == 1:
                        array = order.ordenamiento_shell_atributo_ascendente(array, attribute)
                    else:
                        array = order.ordenamiento_shell_atributo_descendente(array, attribute)
                else:
                    raise ValueError(f"Método de ordenamiento '{metodo}' no válido")
                self.toList(array)
                return self
        return None

    
    def busqueda_secuencial(self, data):
        list = LinkedList()
        if self.isEmpty:
            raise LinkedEmpty('Linked empty')
        else:
            array = self.toArray
            for i in range(0, len(array)):
                if array[i] == data:
                    list.add(array[i], list._length)
        return list 
    
    def busquedaBinaria_numeros(self, array, value):
        left = 0
        right = len(array) - 1
        while left <= right:
            middle = (left + right) // 2
            if array[middle] == value:
                return middle
            elif array[middle] < value:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    
    def busquedaBinaria(self, list, attribute, value):
        if self.isEmpty <= 1:
            array = list.toArray
            left = 0
            rigth = len(array) - 1
            while left <= rigth:
                middle = (left + rigth) // 2
                current = array[middle]
                if getattr(array[middle], attribute) == value:
                    return current
                elif getattr(array[middle], attribute) < value:
                    left = middle + 1
                else:
                    rigth = middle - 1
        return -1

    def busquedaLinealBinariaAtributo(self, lista, atributo, valor):
        lista_auxiliar = LinkedList()
        # arr = lista.ordenamiento_atributo("Quick", attribute = atributo, type=2)
        lista.ordenamiento_atributo("Quick", attribute = atributo, type=2)
        array = lista.toArray
        # array = arr.toArray 
        print("\n\n\n\natributo", atributo)
        izquierda = 0
        derecha = len(array) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if getattr(array[medio], atributo) == valor:
                lista_auxiliar.add(array[medio])
                izq = medio - 1
                while izq >= 0 and getattr(array[izq], atributo) == valor:
                    lista_auxiliar.add(array[izq])
                    izq -= 1
                der = medio + 1
                while der <= derecha and getattr(array[der], atributo) == valor:
                    lista_auxiliar.add(array[der])
                    der += 1
                break
            elif getattr(array[medio], atributo) < valor:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return lista_auxiliar


    def busquedaLinealBinariaNumeros(self, lista,valor):
        lista_auxiliar = LinkedList()
        array = lista.toArray
        izquierda = 0
        derecha = len(array) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if array[medio] == valor:  
                lista_auxiliar.add(array[medio])
                izq = medio - 1
                while izq >= 0 and array[izq]== valor:
                    lista_auxiliar.add(array[izq])
                    izq -= 1
                der = medio + 1
                while der <= derecha and array[der] == valor:
                    lista_auxiliar.add(array[der])
                    der += 1
                break
            elif array[medio] < valor:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return lista_auxiliar