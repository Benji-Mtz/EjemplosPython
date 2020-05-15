from bs4 import BeautifulSoup
import requests
import pandas as pd 

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

url = 'https://alcorconhoy.com/estadisticas-coronavirus-covid-19'
pagina = requests.get(url)
soup = BeautifulSoup(pagina.content, 'html.parser')
#Ciudades
cud= soup.findAll('div', class_='td-covid-country-name')
ciudades=list()
for i in cud:
    ciudades.append(i.text)
#Casos confirmados
cf= soup.findAll('div', class_='td-covid-confirmed')
casosConfirmados=list()
for i in cf:
    casosConfirmados.append(i.text)
#Muertes
mt= soup.findAll('div', class_='td-covid-deaths')
muertes=list()
for i in mt:
    muertes.append(i.text)
#Recuperados
recu= soup.findAll('div', class_='td-covid-recovered')
recuperados=list()
for i in recu:
    recuperados.append(i.text)
#Casos Activos
ca= soup.findAll('div', class_='td-covid-active')
casosActivos=list()
for i in ca:
    casosActivos.append(i.text)
ciudades.pop(0)
casosConfirmados.pop(0)
muertes.pop(0)
recuperados.pop(0)
casosActivos.pop(0)
resultadofinal= pd.DataFrame({'Ciudad':ciudades,'Casos Confirmados':casosConfirmados,'Muertes':muertes,'Casos Recuperados':recuperados,'Casos Activos':casosActivos})

print(resultadofinal.loc[:][:])