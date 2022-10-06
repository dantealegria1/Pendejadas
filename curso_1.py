print("-------------------")
print("Operaciones")
print(10/3)
print(10-3)
print(10*3)
print(10+3)
print(10//3)
print(10**3)
print(10&2)
print("--------------------")
print("input")
a=int(input("ingrese un numero"))
#imprima si es par 
if(a%2==0):
    print("es par")
else:
    print("es impar")
print("--------------------")
print("Mayuscula")
msg=input("ingrese una palabra")
print(msg.upper())
print(msg.lower())
print("--------------------")
print("Reemplazar")
print(msg.replace("a","e").upper())
print(msg.count("a"))
print(msg(-1))
print("--------------------")
print("Listas")
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista)
print(lista[0])
print("--------------------")
edad=input("ingrese su edad")
edad_nueva=int(edad)+10
print("su edad en 10 años sera",edad_nueva)


