
class ShellSort:

    def ordenamiento_shell_atributo_ascendente(self, arr, attribute):
        interval = len(arr) // 2
        while interval > 0:
            for i in range(interval, len(arr)):
                temp = arr[i]
                j = i
                while j >= interval and getattr(arr[j - interval], attribute) > getattr(temp, attribute):
                    arr[j] = arr[j - interval]
                    j -= interval
                arr[j] = temp
            interval //= 2
        return arr 

    def ordenamiento_shell_atributo_descendente(self, arr, attribute):
        interval = len(arr) // 2
        while interval > 0:
            for i in range(interval, len(arr)):
                temp = arr[i]
                j = i
                while j >= interval and getattr(arr[j - interval], attribute) < getattr(temp, attribute):
                    arr[j] = arr[j - interval]
                    j -= interval
                arr[j] = temp
            interval //= 2
        return arr 


    def ordenamiento_shell_numeros_ascendente(self, arr):
        interval = len(arr) // 2
        while interval > 0:
            for i in range(interval, len(arr)):
                temp = arr[i]
                j = i
                while j >= interval and arr[j - interval] > temp:
                    arr[j] = arr[j - interval]
                    j -= interval
                arr[j] = temp
            interval //= 2
        return arr 

    def ordenamiento_shell_numeros_descendente(self, arr):
        interval = len(arr) // 2
        while interval > 0:
            for i in range(interval, len(arr)):
                temp = arr[i]
                j = i
                while j >= interval and arr[j - interval] < temp:
                    arr[j] = arr[j - interval]
                    j -= interval
                arr[j] = temp
            interval //= 2
        return arr