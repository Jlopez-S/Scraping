from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://gamaenlinea.com/CUIDADO-PERSONAL/c/004'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Productos

product = soup.find_all('a', class_='product__list--name')

productos = list()

for i in product:
    productos.append(i.text)


# Precios de los Productos

price_product = soup.find_all('div', class_='from-base-price-value')

prec_productos = list()

for i in price_product:
    prec_productos.append(i.text)

datos = pd.DataFrame({'Producto': product, 'Precio':price_product})

print(datos)
