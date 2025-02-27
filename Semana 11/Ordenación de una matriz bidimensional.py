# Programa 2: Ordenación de una Matriz Bidimensional en un programa interactivo con el usuario
print()
print("°Ordenar en una Matriz Bidimensional°")
print()
#definimos una función para ordenar una fila con Bubble Sort
def buble_sort(fila):
    cantidad_num = len(fila) #obtiene el número de elementos de la fila
    for recorrido in range(cantidad_num): #este bucle for va a recorrer toda la fila por la cantidad de números(las etiquetas son para comprender mejor como funciona)
        for posicion in range(0, cantidad_num - recorrido - 1): #el siguiente bucle for se compara los elementos e intercambia si el orden es incorrecto
            if fila[posicion] > fila[posicion+1]: #determina si un número es mayor que otro para intercambiarlo por el siguiente
                fila[posicion], fila[posicion+1] = fila[posicion+1], fila[posicion]
    return fila

#Se agrega una función par ordenar una fila específica
def ordenar_matriz(matriz,fila0):
    if 0 <= fila0 < len(matriz): #aqui se verificara si la fila que se ingresa esta dentro de los parámetros de la matriz
        matriz[fila0] = buble_sort(matriz[fila0]) #aqui llamara a Bubble_sort para ordenar la fila
    else:
        print("La fila no existe ingrese un numero que pertenezca en la fila de la matriz")# de lo contrario el número ingresado será invalido
    return matriz

#Esta es la matriz (3x3) que se le asignara el orden
matriz =[
    [90, 2, 74,],
    [31, 50, 7,],
    [66, 23, 2,],
]
#agregamos una función para que se imprima la matriz y el usuario la pueda ver
def imprimirmorg(matriz):
    for fila in matriz:#el bucle for recorrerá todas las filas
        print(fila)

#mostramos al usuario la matriz para que elija la fila que desea modificar
print("°Matriz original°:")
imprimirmorg(matriz)

#ordenamos al usuario que elija la fila que va a modificar
fila_ordenada = int(input("\nPorfavor ingresa el numero de la fila (0 a 2) que deseas ordenar: "))
update = ordenar_matriz(matriz,fila_ordenada)# se ordena la fila elegida y actualiza la matriz

print()
#Aqui mostraremos al usuario la matriz que se ha ordenada correctamente
print("\nMatriz ordenada:")
imprimirmorg(update)