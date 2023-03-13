
#Realizado por @Karen
#Bienvenida

print ("------////EJERCICIO RESOLVER PROBELMAS////------ ")
nombre= input("Hola! Ingresa tu nombre")
print ("Bienvenid@", nombre)


''' Creamos una funcion de validar y en esta un while donde se 
repita un mensaje hasta que cumpla la condicion'''

def validar(mensaje): #Se envia como parametro mensaje 

    while True:
        try:
            
            datos = float(input("Ingrese" + mensaje)) #Se concatena un mensaje para todos 
            return datos
        except ValueError: #Si no se cumple se muestra el mensaje de error
            print( nombre, "," , "El dato de ingreso debe ser un numero entero o decimal")

#Creo las variables y el input para que se peudan ingresar por consola 

largo =validar ("el largo en metros") #Se pone la variable y el nombre del metodo que es validar
ancho= validar(" el ancho en metros")
caja = validar("los metros cuadrados por caja")
precio = validar(" el precio por metros cuadrados")

#Se hace la operacion 

'''Se hace la operacion para sabver el 
precio de la caja por metro '''
PrecioCaja=caja*precio

''' Se ahce la operacion para saber cuanto mide el cuarto'''
Cuarto= largo*ancho

''' Se hace la division de lo que mide el cuarto por el metro de la caja'''
Cajas=Cuarto/caja

''' El precio total seria el resualtdo 
anterior * el precio de la caja anteriormete sacado '''
precioTotal=Cajas*PrecioCaja

#Se imprimen los resultados 
print( nombre, "," , "El total de las cajas que se necesitan son :", Cajas)
print( nombre, "," ,  "El gasto total es:" , precioTotal)