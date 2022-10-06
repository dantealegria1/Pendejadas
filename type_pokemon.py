import requests
import webbrowser
opcion=int(input("1. nombre del pokemon/ 2. tipo de pokemon/" ))
if opcion==1:
    pokemon=input("introduce el nombre de un pokemon: ")
    url="https://www.pokemon.com/us/pokedex/"+pokemon
    res=requests.get(url)
    print(res)
    webbrowser.open(url)
    if res.status_code != 200:
        print("pokemon no encontrado")
        exit()
if opcion==2:
    tipo=input("introduce el tipo de pokemon: ")
    url="https://pokestop.io/type/"+tipo
    res=requests.get(url)
    print(res)
    webbrowser.open(url)
    if res.status_code != 200:  
        print("tipo no encontrado")
        exit()
    

