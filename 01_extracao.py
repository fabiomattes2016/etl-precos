import time
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


precos = []

url_boi = "https://www.melhorcambio.com/boi-hoje"
url_soja = "https://www.melhorcambio.com/soja-hoje"
url_milho = "https://www.melhorcambio.com/milho-hoje"
url_cafe = "https://www.melhorcambio.com/cafe-hoje"
url_suino = "https://www.melhorcambio.com/suino-hoje"
url_bezerro = "https://www.melhorcambio.com/bezerro-hoje"

chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service, options=chrome_options)

print("Iniciando extração de dados! Aguarde...")

# Boi
print("Recuperando preço do Boi...")
nav.get(url_boi)
time.sleep(5)
preco_boi_arroba = nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
now = datetime.now()
precos.append({"ativo": "Boi", "preco": preco_boi_arroba, "data_hora": datetime.timestamp(now)})

# Soja
print("Recuperando preço da Soja...")
nav.get(url_soja)
time.sleep(5)
preco_soja_saca = nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
now = datetime.now()
precos.append({"ativo": "Soja", "preco": preco_soja_saca, "data_hora": datetime.timestamp(now)})

# Milho
print("Recuperando preço do Milho...")
nav.get(url_milho)
time.sleep(5)
preco_milho_saca = nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
now = datetime.now()
precos.append({"ativo": "Milho", "preco": preco_milho_saca, "data_hora": datetime.timestamp(now)})

# Café
print("Recuperando preço do Café...")
nav.get(url_cafe)
time.sleep(5)
preco_cafe_saca = nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
now = datetime.now()
precos.append({"ativo": "Café", "preco": preco_cafe_saca, "data_hora": datetime.timestamp(now)})

# Suino
print("Recuperando preço do Suino...")
nav.get(url_suino)
time.sleep(5)
preco_suino_quilo = nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
now = datetime.now()
precos.append({"ativo": "Suino", "preco": preco_suino_quilo, "data_hora": datetime.timestamp(now)})

# Bezerro
print("Recuperando preço do Bezerro...")
nav.get(url_bezerro)
time.sleep(5)
preco_bezerro_cabeca = nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
now = datetime.now()
precos.append({"ativo": "Bezerro", "preco": preco_bezerro_cabeca, "data_hora": datetime.timestamp(now)})

time.sleep(5)
nome_arquivo = 'extracao/precos_ativos_bruto.csv'
campos = ['ativo', 'preco', 'data_hora']

with open(nome_arquivo, 'w', newline='', encoding='utf8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=campos)
    writer.writeheader()
    writer.writerows(precos)

print(f"Dados exportados para o arquivo {nome_arquivo}")

time.sleep(15)
nav.quit()
