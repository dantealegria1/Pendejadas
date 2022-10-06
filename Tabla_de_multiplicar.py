#tabla de multiplicar de un numero
import math
print("-----------------------------------------")
print("Tabla de multiplicar de un numero")
numero=int(input("Introduce un numero: "))
limite=int(input("Hasta que numero quieres la tabla: "))
inicio=int(input("Desde que numero quieres la tabla: "))
for i in range(inicio,limite+1):
    print(numero,"x",i,"=",numero*i)
    #numero=lo que ingrese el usuario
    #i empeiza por 1 y termina en el numero deseado
print("-----------------------------------------")
print("Volumen del cilindro")
#Volumen de un cilindro
def altura():
    altura=float(input("Introduce la altura del cilindro: "))
    return altura
def radio():
    radio=float(input("Introduce el radio del cilindro: "))
    return radio
def volumen():
    volumen=math.pi*(radio()**2)*altura()
    return volumen
print("El volumen del cilindro es: ",volumen())