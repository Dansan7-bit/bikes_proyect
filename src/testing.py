from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Especifica la ruta de tu ChromeDriver
chrome_driver_path = r'C:\Users\FX516\Downloads\chromedriver-win64\chromedriver.exe'

# Configurar el servicio de ChromeDriver
service = ChromeService(executable_path=chrome_driver_path)

# Inicializar el navegador Chrome con el servicio configurado
driver = webdriver.Chrome(service=service)

# Abrir la página web
url = 'https://ourworldindata.org/grapher/electric-car-sales-share?tab=table&time=2012'
driver.get(url)

try:
    # Esperar explícitamente a que la tabla esté presente
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))

    # Obtener el contenido HTML de la página
    html = driver.page_source

    # Procesar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extraer la tabla
    table = soup.find('tbody')
    if table:
        df = pd.read_html(str(table))[0]
        print(df.head())
    else:
        print("No se encontró ninguna tabla en la página.")
    
    # Pausar para inspeccionar el navegador antes de cerrarlo
    input("Presiona Enter para cerrar el navegador...")
except Exception as e:
    print(f"Error durante la espera o el procesamiento de la página: {e}")
finally:
    # Cerrar el navegador
    driver.quit()
