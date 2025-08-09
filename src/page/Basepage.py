from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from configparser import ConfigParser
import os

class Basepage:

    def setup_driver(self ):
        options = Options()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        wait = WebDriverWait(driver, 10)


        return driver,wait

    def teardown(self, context):
        context.driver.quit()















































#behave src/features




"""        config = ConfigParser()
        base_dir = os.getcwd()  # el cwd (ej. Proyecto_python)
        config_path = os.path.join(base_dir, path)

        print("Leyendo archivo:", config_path)
        files_read = config.read(config_path)

        if not files_read:
            raise FileNotFoundError(f"No se pudo leer el archivo: {config_path}")

"""





"""class Basepage():

    
    def get_driver(path="settings/chrome-properties.cfg"):

        config = configparser.ConfigParser()
        config.read(path)

        options = Options()

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        
        driver.get('https://www.icbc.com.ar/personas/productos-servicios/canales-servicio/access-banking')
        driver.quit()

   



def main():
    pepe = Basepage()
    pepe.get_driver()

main() 


"""
















"""    def get_driver(config_path="config/chrome-properties.cfg"):
        config = configparser.ConfigParser()
        config.read(config_path)

        options = webdriver.ChromeOptions()
        
        # Leer argumentos
        if config.has_section("arguments"):
            for key, value in config.items("arguments"):
                if value.lower() == "true":
                    options.add_argument(f"--{key}")

        # Crear el driver
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        # Maximizar si se pide
        if config.getboolean("driver", "maximize", fallback=False):
            driver.maximize_window()
"""