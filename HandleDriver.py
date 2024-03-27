from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class HandleDriver:
    def __init__(self):
        self.chrome_driver = None

    def initialize_driver(self, headless=False):
        ''' inicia el driver '''
        chrome_options = webdriver.ChromeOptions()

        if headless:
            chrome_options.add_argument('--headless')  # Configura el modo headless
            chrome_options.add_argument('--disable-gpu')  # Desactiva la GPU para evitar problemas en algunos sistemas

        self.chrome_driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()
            ),
            options=chrome_options
        )

    def get_driver(self):
        ''' retorna el driver '''
        return self.chrome_driver
