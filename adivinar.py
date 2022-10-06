#adivinar un numero 
import random
limite= int(input("ingrese el limite: "))
numero=random.randint(1,limite)
guess=int(input("adivine el numero: "))
intentos=1;
while guess != numero and guess != 6:
    if guess<numero:
        print("el numero es mayor")
    else:
        print("el numero es menor")
    print("-------------------------")
    guess=int(input("adivine el numero: "))
    intentos=intentos+1
    print("numero de intentos: ",intentos)
    if intentos==6:
        print("el numero era",numero)
        break
    if guess==numero:
        print("adivino el numero en",intentos,"intentos")

        
