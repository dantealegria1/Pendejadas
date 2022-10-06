#programa de apuestas a un dado 
from pickle import FALSE
import random

Presupuesto=int(input("Introduce tu presupuesto: "))

def aleatorio():
    Dado=random.randint(1,6)
    return Dado

def pedirNumero():
    numero=int(input("Introduce un numero: "))
    while numero>6 or numero<1:
        print("El numero debe estar entre 1 y 6")
        numero=int(input("Introduce un numero: "))
    return numero

def pedirApuesta():
    Apuesta=int(input("Introduce una apuesta: "))
    while Apuesta>Presupuesto:
        print("No puedes apostar mas de lo que tienes")
        Apuesta=int(input("Introduce una apuesta: "))
    return Apuesta

def jugar(numero1,Apuesta1,Dado1,Presupuesto1):
    if numero1==Dado1:
        Presupuesto1=Presupuesto1+Apuesta1
        print("Has ganado")
        print("Tu presupuesto es: ",Presupuesto1)
    else:
        Presupuesto1=Presupuesto1-Apuesta1
        print("Has perdido")
        print("Tu presupuesto es: ",Presupuesto1)

while Presupuesto>0:
    print("--------------")
    print("JUEGA AL DADO")
    print("--------------")
    numero=pedirNumero()
    Apuesta=pedirApuesta()
    Dado=aleatorio()
    jugar(numero,Apuesta,Dado, Presupuesto)
    if numero!=Dado:
        Presupuesto=Presupuesto-Apuesta
    else:
        Presupuesto=Presupuesto+Apuesta
        print("el dado era: ",Dado)
