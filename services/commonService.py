from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CommonService():

    def __init__(self, driver):
        self.driver = driver

    def WaitAndClick(self, tuple, seconds=10):       
      try:
        WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(tuple)).click()
      except TimeoutException: # dado esta excepcion, la gestiono enviando otra excepcion con msj personalizado.
        raise TimeoutError("El elemento no se encontró dentro del tiempo especificado")

    def WaitAndSendKeys(self, tuple, keys, seconds=10):       
        WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(tuple)).send_keys(keys)

    def WaitAndFindElements(self, tuple, seconds=10):
            WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(tuple))
            return self.driver.find_elements(tuple[0], tuple[1])
    
    def WaitAndFindElement(self, tuple, number, seconds=10):
            ''' retorna un elemento especificado con [num] '''
            (by, value) = tuple
            WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(tuple))
            return self.driver.find_element(by, value + f'[{number}]')
    
    def WaitAndText(self, tuple, seconds=10):
            WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(tuple))
            return self.driver.find_element(tuple).text
            
    def isPresent (self, tuple, seconds=3):
      ''' retorna un boleando en funcion de si esta presente o no el elemento dado <br/> recibe una tupla porque los locator usan find_element al momento de ejecucion y retornan excepcion en caso negativo '''
      try:
        WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(tuple))
        return True
      except TimeoutException as e:
        return False
      
    def isVisible (self, tuple, seconds=3):
      ''' Estar visible es distinto a estar presente. '''
      try:
        WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(tuple))
        return True
      except TimeoutException as e:
        return False
