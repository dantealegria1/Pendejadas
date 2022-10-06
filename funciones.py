#crear una funcion que suma dos numeros
def suma(a,b):
    return a+b

#crear una funcion que resta dos numeros
def resta(a,b):
    return a-b

#funcion que multiplica dos numeros
def multiplicacion(a,b):
    return a*b
    
#funcion que divide dos numeros
def division(a,b):
    return a/b

#incio del programa

a=int(input("ingrese un numero: "))
b=int(input("ingrese un numero: "))
opciones=int(input("1. suma/ 2. resta/ 3. multiplicacion/ 4. division: "))
if opciones==1:
    print(suma(a,b))
elif opciones==2:
    print(resta(a,b))
elif opciones==3:
    print(multiplicacion(a,b))
elif opciones==4:
    print(division(a,b))
else:
    print("opcion no valida")

