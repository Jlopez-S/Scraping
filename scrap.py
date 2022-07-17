from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


urls = 'https://gamaenlinea.com/CUIDADO-PERSONAL/c/004?q=%3Arelevance%3AmanufacturerName%3ACOLGATE'
page = requests.get(urls)
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

# IVAS productos
iva_product = soup.find_all('div', class_='from-tax-value')

ivas_productos = list()

for i in iva_product:
    ivas_productos.append(i.text)

# Precio Total
prec_total = soup.find_all('div', class_='from-price-value')

prec_totales= list()

for i in prec_total:
    prec_totales.append(i.text)


def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)


datos = pd.DataFrame({'Producto': product, 'Precio': price_product, 'IVA': iva_product, 'Precio Total': prec_total})


datos.to_excel('excelciorgama.xlsx')
print(datos)
