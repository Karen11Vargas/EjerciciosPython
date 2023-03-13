numbers = [1,2,3,4,5,6,7] #Arreglo
par = 0  #Se inicalizan en 0 las variables 
impar = 0

for dato in numbers:  
    if dato % 2 == 0:   # Condicional de que si un elemento en la posicion se divide 
                        #  entre dos y da 0 es por que es mumero par
        par = par + dato 
    else:
        impar = impar + dato

print("Suma de números impares:",impar)
print("Suma de números pares:",par)