class MergeSort:
            
    def ordenamiento_merge_ascendente_numeros(self, arr):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        left = self.ordenamiento_merge_ascendente_numeros(arr[:mid])
        right = self.ordenamiento_merge_ascendente_numeros(arr[mid:])
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result

    def ordenamiento_merge_descendente_numeros(self, arr):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        left = self.ordenamiento_merge_descendente_numeros(arr[:mid])
        right = self.ordenamiento_merge_descendente_numeros(arr[mid:])
        result = []
        while left and right:
            if left[0] > right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result

    def ordenamiento_merge_ascendente_atributo(self, arr, attribute):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        left = self.ordenamiento_merge_ascendente_atributo(arr[:mid], attribute)
        right = self.ordenamiento_merge_ascendente_atributo(arr[mid:], attribute)
        result = []
        while left and right:
            if getattr(left[0], attribute) < getattr(right[0], attribute):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result

    def ordenamiento_merge_descendente_atributo(self, arr, attribute):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        left = self.ordenamiento_merge_descendente_atributo(arr[:mid], attribute)
        right = self.ordenamiento_merge_descendente_atributo(arr[mid:], attribute)
        result = []
        while left and right:
            if getattr(left[0], attribute) > getattr(right[0], attribute):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result