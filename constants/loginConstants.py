from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginConstants():

    def __init__(self, driver):
        self.driver = driver

    def txt_username(self):
        return (By.XPATH, "//*[@id='username']")
    
    def txt_password_field (self): 
        return (By.XPATH, "//*[@id='password']")

    def btn_submit (self):
        return (By.XPATH, "//button[@type='submit']")
    
    def human_verification(self):
        ''' tupla del titular de la pantalla de verificacion anti bots '''
        return (By.XPATH, "//h1[contains(.,'do a quick security check')]")
    
    def email_verification(self):
        ''' tupla del titular de la pantalla de inicio de sesion sopechoso, verificacion por email '''
        return (By.XPATH, "//h1[contains(.,'Vamos a hacer una comprobación rápida')]")
    
    def alert(self):
        ''' tupla de cualquier elemento de alerta luego de intentar iniciar sesion '''
        return (By.XPATH, "//*[@id='guest-input__message']")
    
    def isVisible (self, tuple, seconds=10):
      ''' Estar visible es distinto a estar presente. '''
      try:
        WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(tuple))
        return True
      except TimeoutException as e:
        return False
