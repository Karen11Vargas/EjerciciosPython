
"""def saludar(nombre):
    return "Hola {} aqui".format(nombre)
    print('Ingresa nombre')
    nombre = input()

    print(saludar(nombre))"""


def salarioSemana(horas, salarioHoras, trabajo): #Se crean los parametros como las horas, el salario y el tipo de trabajo

    salario = horas * salarioHoras #Operacion para saacar el salrio por dia
    salario = salario * 7 #Operacion para sacar el salario por semana
    print("El sueldo de un", trabajo , "es: ",salario) # Imprimir el mesanje con el parametro de trabajo

salarioSemana(8, 5000, "Doctor") #Se ingresan los parametros, horas, salario y tipo de profesion 
salarioSemana(4, 2000, "Jardinero")


