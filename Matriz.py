matriz1 = [ [1, 2, 3], [7, 8, 9], [13, 14, 15] ]
matriz2 = [ [4, 5, 6], [10, 11, 12], [16, 17, 18] ]
matriz3 = [ [1, 2, 3], [7, 8, 9], [13, 14, 15] ]

for fila, dato in enumerate(matriz1):
    for columna, dato1 in enumerate(dato):
        matriz3[fila][columna]=dato1+matriz2[fila][columna]
print(matriz1, "+", matriz2, " = ", matriz3)

