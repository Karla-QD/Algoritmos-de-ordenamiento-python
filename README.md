# Algoritmos-de-ordenamiento-python

### Burbuja:

El algoritmo de ordenamiento de burbuja funciona comparando pares de elementos adyacentes de la lista y, si están en el orden equivocado
(el primer elemento es mayor que el segundo), intercambia esos elementos. Este proceso se repite para cada par de elementos adyacentes en la lista, 
moviendo gradualmente el elemento más grande hacia el final de la lista. En cada iteración, se reduce el límite del ciclo interno, ya que el elemento
más grande ya está en su posición correcta. El algoritmo repite este proceso hasta que no se realicen más intercambios en la lista, lo que indica que
la lista está ordenada.

### Quicksort

La función quickSort utiliza la función particion para dividir la lista en dos sub-listas alrededor de un pivote, y luego llama a sí misma recursivamente
para ordenar las dos sub-listas.Este proceso se repite hasta que la lista se divide en sub-listas de un solo elemento, momento en el que la lista se considera ordenada.
