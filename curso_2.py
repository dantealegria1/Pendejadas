#acronimos de una frase
print("-------------------------")
print("Acronimos")
print("-------------------------")
frase=input("ingrese una frase: ")
frase=frase.upper()
frase=frase.split()
print(frase)
acronimo=""
for palabra in frase:
    acronimo=acronimo+palabra[0]+"."
print(acronimo)
