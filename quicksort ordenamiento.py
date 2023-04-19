def quickSort(a:list[int],izquierda, derecha) -> int:
    if izquierda < derecha:
        mitad = particion(a, izquierda, derecha)
        quickSort(a, izquierda, mitad)
        quickSort(a, mitad + 1, derecha)


def particion(a:list[int],izq,derec) -> int:
    pivote = a[izq]
    while True:
        while a[izq] < pivote:
            izq += 1
        while a[derec] > pivote:
            derec -= 1
        if izq >= derec: 
            return derec
        else:
            a[izq], a[derec] = a[derec], a[izq]
        izq  += 1
        derec -= 1
        
a = [5, 1, 2, 1, 1, 3, 5, 1, 5, 1, 99, 231, 234, 12, 121 ]
print("Antes de ordenarlo: ")
print(a)
quickSort(a, 0, len(a) - 1)
print("Después de ordenarlo: ")
print(a)