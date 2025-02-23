from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from rich.progress import Progress
from rich import print

def scrape_celulares():
    # Configuración del driver (en este ejemplo se utiliza Chrome)
    driver = webdriver.Chrome()  # Asegúrate de tener chromedriver instalado y en el PATH

    # URL de inicio
    start_url = "https://miportal.entel.cl/personas/catalogo/celulares"
    driver.get(start_url)

    # Lista para almacenar los URLs encontrados
    urls = []

    # Crear un objeto Progress para mostrar el avance
    with Progress() as progress:
        # Definir una tarea para mostrar el avance del scraping
        task = progress.add_task("[cyan]Scrapeando...", total=25)

        page_counter = 0
        while True:
            # Esperar a que los elementos de interés se carguen
            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'product-col')]//a")))

            # Extraer todos los href de los <a> dentro de un <div> que contiene "product-col" en la clase.
            links = driver.find_elements(By.XPATH, "//div[contains(@class, 'product-col')]//a")
            for link in links:
                href = link.get_attribute("href")
                urls.append(href)  # Agregar el URL a la lista

            page_counter += 1  # Incrementar contador de páginas

            # Mostrar cuántas URLs se han encontrado hasta ahora
            progress.update(task, advance=len(links))  # Avanzamos el progreso por la cantidad de links encontrados

            # Imprimir el número de URLs encontradas hasta ahora
            print(f"[bold green]URLs encontradas hasta ahora: {len(urls)}[/bold green]")

            # Buscar el enlace a la siguiente página (botón que contiene "page-right")
            try:
                # Esperar hasta que el enlace sea visible
                next_page_link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//a[@id="action-PRODUCT_LIST_LOAD_MORE" and contains(@class, "page-right")]'))
                )
                # Extraer el href del enlace
                next_page_url = next_page_link.get_attribute('href')
                print(f"URL siguiente página: {next_page_url}")
                
                # Navegar a la siguiente página
                driver.get(next_page_url)
                # Esperar unos segundos para que la siguiente página cargue
                time.sleep(5)
            except Exception as e:
                print("[bold red]No se encontró el botón de siguiente, finalizando el scraping.[/bold red]")
                break

        # Guardar los URLs encontrados en un archivo .txt
        with open("urls.txt", "w") as file:
            for url in urls:
                file.write(url + "\n")
            
        # Mostrar el número total de URLs guardadas
        print(f"[bold blue]Se han guardado {len(urls)} URLs en 'urls.txt'[/bold blue].")
    
    driver.quit()

if __name__ == "__main__":
    scrape_celulares()
