import requests
import webbrowser
dato="https://api.kanye.rest"
response=requests.get(dato)
print(response)
jsonYe=response.json()
dato=jsonYe["quote"]
print(dato, "-Kanye West")
