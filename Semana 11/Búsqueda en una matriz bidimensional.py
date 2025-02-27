# Programa 1: Búsqueda en una Matriz Bidimensional en un programa interactivo con el usuario
print()
print("°Búsqueda en una Matriz Bidimensional°")
print()
#Damos una función para buscar un valor en la matriz
def encontrar_num(matriz, num):

    #Usamos un bucle for para analizar las filas y encontrar el número
    for fila in range(len(matriz)):

        #Usamos otro bucle for para analizar las columnas de las filas
        for columna in range(len(matriz[fila])):

            #Se compara el valor asignado con la posición
            if matriz[fila][columna] == num:

                #Aqui afirmara si el numero de la fila y la columna se encontró
                return fila, columna

#Matriz bidimensional de 3x3
matriz = [
    [11, 10, 15,],
    [20, 25, 30,],
    [35, 40, 45,],
]

#mostramos la matriz al usuario para que sepa que números puede escoger
print("Matriz:")
for fila in matriz:
    print(fila)

#Solicitamos un numero al usuario
print()
buscar_num = int(input("Porfavor ingrese un numero de la matriz de arriba: "))

#llamamos a la función para saber si el número se encontró
num_encontrado = encontrar_num(matriz, buscar_num)

#finalmente, damos la respuesta al usuario sobre la ubicación del número que solicito o de lo contrario si el mismo no se encuentra en la matriz
if num_encontrado:
    print(f"El numero {buscar_num} si se encuentra en la matriz, exactamente en la posición: {num_encontrado}")
else:
    print(f"El numero {buscar_num} no se encuentra en la matriz.")