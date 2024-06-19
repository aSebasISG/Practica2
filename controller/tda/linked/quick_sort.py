class QuickSort:
    
    def ordenamiento_quick_numeros_ascendente(self, array):
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return self.ordenamiento_quick_numeros_ascendente(left) + middle + self.ordenamiento_quick_numeros_ascendente(right)
    
    def ordenamiento_quick_numeros_descendente(self, array):
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x > pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x < pivot]
        return self.ordenamiento_quick_numeros_descendente(left) + middle + self.ordenamiento_quick_numeros_descendente(right)
    
    def ordenamiento_quick_atributo_ascendente(self, arr, attribute):
        if len(arr) <= 1:
            return arr
        pivot = getattr(arr[len(arr) // 2], attribute)
        left = [x for x in arr if getattr(x, attribute) < pivot]
        middle = [x for x in arr if getattr(x, attribute) == pivot]
        right = [x for x in arr if getattr(x, attribute) > pivot]
        return self.ordenamiento_quick_atributo_ascendente(left, attribute) + middle + self.ordenamiento_quick_atributo_ascendente(right, attribute)
    
    def ordenamiento_quick_atributo_descendente(self, arr, attribute):
        if len(arr) <= 1:
            return arr
        pivot = getattr(arr[len(arr) // 2], attribute)
        left = [x for x in arr if getattr(x, attribute) > pivot]
        middle = [x for x in arr if getattr(x, attribute) == pivot]
        right = [x for x in arr if getattr(x, attribute) < pivot]
        return self.ordenamiento_quick_atributo_descendente(left, attribute) + middle + self.ordenamiento_quick_atributo_descendente(right, attribute)