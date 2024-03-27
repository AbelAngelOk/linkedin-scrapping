from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CompanyConstants():

    def __init__(self, driver):
        self.driver = driver

    def acerca_de(self):
        ''' cantidad de empresas '''
        return (By.XPATH, "//li[contains(.,'Acerca de')]//a/..")
    
    def ls_datos_adicionales(self):
        'valores con datos adicionales de empresa'
        return (By.XPATH,"//dd")
    
    def ls_claves_de_datos_adicionales(self):
        return (By.XPATH, "//div[contains(@id,'ember')]//dt")
    
    def ls_valores_de_datos_adicionales(self):
        return (By.XPATH,"//div[contains(@id,'ember')]//dd")