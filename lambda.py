'''
#Forma tradicional de una funcion
def resta (num):
      result= num - 10
      return result
print(resta(30))


#Funcion lambda
resta = lambda num: num-10
print(resta(30))


#Map

#1
numeros = [1,2,3,4,5,6]
resultado=[]

for datos in numeros:
    resultado.append(datos*5)
print(resultado)

#2
def mult(datos):
    return datos*10
print((list(map(mult,numeros))))

#3
print(list(map((lambda datos: datos*11),numeros)))


#Filter

numeros = [1,2,3,4,5,6]
pares=[]

for datos in numeros:
    if (datos %2 == 0):
        pares.append(datos)
print(pares)

def par(numero):
    return numero % 2 !=0
print(list(filter(par, numeros)))


print(list(filter((lambda numeros: numeros %2 ==0 ), numeros)))



#Reduce
import functools

numeros = [1,2,3,4,5,6]
result=0

for datos in numeros:
    result = result + datos
print(result)

def suma(datos):
    result= result + datos
print(result)

print(str(functools.reduce((lambda a, b: a+b), numeros)))

'''

#Funciones para numeros
color= "Morado azul"
print(color.split(" "))
