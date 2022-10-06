import random
PresupuestoInicial=15
Dado=random.randint(1,6)
numero=int(input("Introduce un numero: "))
while numero>6 or numero<1:
    print("El numero debe estar entre 1 y 6")
    numero=int(input("Introduce un numero: "))

Apuesta=int(input("Introduce una apuesta: "))
while Apuesta>PresupuestoInicial:
    print("No puedes apostar mas de lo que tienes")
    Apuesta=int(input("Introduce una apuesta: "))

if numero==Dado:
    PresupuestoInicial=PresupuestoInicial+Apuesta
    print("Has ganado")
    print("Tu presupuesto es: ",PresupuestoInicial)
else:
    PresupuestoInicial=PresupuestoInicial-Apuesta
    print("Has perdido")
    print("Tu presupuesto es: ",PresupuestoInicial)


