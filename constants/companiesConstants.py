from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CompaniesConstants():

    def __init__(self, driver):
        self.driver = driver

    def cant_empresas(self):
        ''' cantidad de empresas '''
        return (By.CLASS_NAME, "reusable-search__result-container")
    
    
