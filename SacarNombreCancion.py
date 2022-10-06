import requests
import lxml.html as html
cancion=input("Ingrese su cancion ")
cancion=cancion.replace(" ", "%20")
urlBusqueda="https://www.lyricsfreak.com/search.php?q="+cancion
respuesta=requests.get(urlBusqueda)
print(respuesta)
htmlresponse=respuesta.content

linksRegex = '//a[@class="song"]/@href'

htmlresponse=htmlresponse.decode("utf-8")
links = html.fromstring(htmlresponse)
links = links.xpath(linksRegex)[0]
print(links)

respuestacancion=requests.get("https://www.lyricsfreak.com"+links)
cancion2=respuestacancion.content.decode("utf-8")
cancion2=html.fromstring(cancion2)

letra=cancion2.xpath('//div[@id="content"]//text()')

for i in letra:
    print(i)
