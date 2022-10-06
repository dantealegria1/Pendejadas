import requests
import webbrowser

url="https://random.dog/woof.json"
response=requests.get(url)
print(response)
jsonDogs=response.json()
dato=jsonDogs["url"]
print(dato)
webbrowser.open(dato)