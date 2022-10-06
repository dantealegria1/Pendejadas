import requests
import webbrowser
print("Random Facts")
print("-------------")
#Frases random
#fuarda la variable de la url
respuestaRequest=requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
#imprime el estado 
print(respuestaRequest)
#imprime el contenido
jsondeRequest=respuestaRequest.json()
dato=jsondeRequest["text"]
print(dato)

print("-------------")
print("Random Cat photos")
print("-------------")
#Fotos de gato
#fuarda la variable de la url
respuestaRequest2=requests.get("https://api.thecatapi.com/v1/images/search")
#imprime el estado
print(respuestaRequest2)
#imprime el contenido
jsondeRequest2=respuestaRequest2.json()
dato2=jsondeRequest2[0]["url"]
print(dato2)

#Abre el navegador con la foto
webbrowser.open(dato2)

