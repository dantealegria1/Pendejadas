from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://www.pokemon.com/us/pokedex/lucario"
res=requests.get(url)
soup=BeautifulSoup(res.content, 'html.parser')

debil=soup.find_all('span', class_='dtm-weakness')
print(debil)

url2="https://bulbapedia.bulbagarden.net/wiki/Lucario_(Pokémon)#Type_effectiveness"
res2=requests.get(url2)
soup2=BeautifulSoup(res2.content, 'html.parser')
weak=soup2.find_all('table', class_='roundy')
print(weak)

url3="https://pokestop.io/type/fighting"
res3=requests.get(url3)
soup3=BeautifulSoup(res3.content, 'html.parser')
weak2=soup3.find_all('table', class_='table table-striped table-bordered table-hover')
print(weak2)