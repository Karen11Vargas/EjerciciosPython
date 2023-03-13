'''#Arreghlos normales, por tipo de dato
numbers = [1,2,3,4,5]
    0,1,2,3,4 
print (numbers[4])

colores = ["Azul", "Morado", 
"Blanco", "Verde"]
print(colores[3])

#Asociativos que incluyen dierentes tipos de datos 
          
          #clave    #atributo
persona = {"nombre":"Valery", "Apellido":"Cardenas","Edad":4,"Estatura": 1.00}

            #Se llama la clave del arreglo
print(persona.get("Apellido"))




persona = {"nombre":"Valery", "Apellido":"Cardenas","Edad":4,"Estatura": 1.00}
numbers = [1,2,3,4,5]

print(len(numbers))
print(len(persona))
print (" ")



#Arreglo multidimencional 

zapatos= [
    ["tenis1", "tenis2", "tenis3"],
    ["tenis4", "tenis5", "tenis6"],
    ["tenis7", "tenis8", "tenis9"]]

print(zapatos[0][0])

# Recorrer Arreglos
persona ={
   "Nombre": [ "Karen",  "Milena", "Sandra"],
   "Apellido":[ "Vargas","Vargas"  ,  "Vargas"],
   "edad":[16, 23,  21]}
print(persona["edad"][0])

for clave, list in persona.items():
    for datos in list:
        print("Estos son las personas", clave, datos) 

        '''

numeros = [16,21,23, 5]
for lugar, dato in enumerate(numeros):
    print ("El lugar es: ", lugar, "- ", dato)