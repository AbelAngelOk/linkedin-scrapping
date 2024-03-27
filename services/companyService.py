from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from constants.companyConstants import CompanyConstants
from services.commonService import CommonService
from bs4 import BeautifulSoup

class CompanyService(CommonService):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CompanyConstants(driver) 

        self.driver = driver
        self.acerca_de = None
        self.algo = None
    
    def AbrirNuevaVentanaCon(self, enlace):
        ''' abre una nueva ventana que redirecciona al enlace y se posiciona sobre ella'''
        if enlace:
            self.driver.execute_script(f"window.open('{enlace}', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
    
    def IrAcercaDe(self):
        ''' Hacer clic en la pestaña "Acerca de"
        precondicion: estar en la pagina linkedin de una empresa '''
        try:
            self.acerca_de = self.WaitAndClick( self.constants.acerca_de() )
            return True
        except NoSuchElementException as e:
            print("Página no disponible, continua con la siguiente", str(e))
            return False
        except TimeoutError as e:
            return False


    def eliminarElementosNoDeseados(self):
        ''' elimina los valores extras que tiene la clave miembros asociados. '''

        for dato in self.WaitAndFindElements( self.constants.ls_datos_adicionales() ):
            if "miembros asociados" in dato.text:
                self.driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", dato)
                break

    def cerrarVentana(self):
        self.driver.close() # cerrar ventana actual
        self.driver.switch_to.window(self.driver.window_handles[0]) # ir(volver) a ventana principal

    # scrape_additional_data
    def recopilacionOpcionalDeDatos(self):
        """ Recopila datos adicionales de la empresa. """
 
        datos_adicionales_empresa = {} # Inicializar el diccionario para almacenar datos adicionales      
        numero_de_datos_a_obtener = self.WaitAndFindElements( self.constants.ls_claves_de_datos_adicionales() ) # Obtener la lista de elementos a partir del tag "dd"

        # Iterar sobre los elementos y recopilar datos
        for dato_index, _ in enumerate(numero_de_datos_a_obtener):
            # Esperar a que el elemento esté presente y obtener su texto
            # nombre_del_campo = self.WaitAndText( (By.XPATH, f"//div[contains(@id,'ember')]//dt[{dato_index + 1}]") )
            nombre_del_campo = self.WaitAndText( self.WaitAndFindElement( self.constants.ls_claves_de_datos_adicionales(), dato_index+1 ) )
            valor_del_campo = self.handleValuesDD( self.WaitAndFindElement( self.constants.ls_valores_de_datos_adicionales(), dato_index+1 ) )
            datos_adicionales_empresa[nombre_del_campo] = valor_del_campo
        return datos_adicionales_empresa
    
    def handleValuesDD(self, locator):
        ''' si el dd tiene varios valores retorna una lista de valores, caso contrario retorna el texto del dd'''
        # (c, v) = locator # separo los elementos de la tupla
        # e = self.driver.find_element(By.XPATH, locator) # busco los elementos del locator
        soup = BeautifulSoup(locator.get_attribute("outerHTML"), "html.parser") # Crear un objeto BeautifulSoup para facilitar el análisis del HTML

        lsli = [] # ls = lista, lsli = lista de li

        if soup.find("ul"):  # Si hay un ul..
            for index, li in enumerate( soup.find_all('li') ): # por cada li..
                 print(f'li {index}:' + str(li))
                 lsli.append( li.get_text(strip=True) ) # agrega el texto del li a la lista.
        else: # Si no hay un ul...
            lsli = soup.find("dd")
            lsli = lsli.get_text(strip=True) # pisa la lista y la reemplaza por el texto de dd

        return lsli # retorna una ls de los valores de cada li o retorna el texto de dd

    def recopilarDatos_VersionChatGPT(self):
        lsdl = self.driver.find_elements(By.XPATH, '//dl') # Encuentra todos los elementos <dl>

        lsdl_soup = []

        # transforma cada dl, uno por uno. (no se puede hacer sobre todos directamente)
        for dl in lsdl:
            # lista de bloques con etiqueta dl transformada a soup.
            dl_soup = BeautifulSoup(dl.get_attribute("outerHTML"), "html.parser")
            lsdl_soup.append(dl_soup) 

        datos_emp = {}  # Diccionario para almacenar los datos
       
        for dl in lsdl_soup: # Itera sobre cada elemento <dl>           
            if dl.find('dt'): # Verifica si el <dl> tiene al menos un <dt>
                ls_dt = dl.find_all('dt') # Encuentra todos los elementos <dt> y <dd> dentro del <dl>
                ls_dd = dl.find_all('dd') # Encuentra todos los elementos <dt> y <dd> dentro del <dl>

                for dt, dd in zip(ls_dt, ls_dd): # Itera sobre los elementos <dt> y <dd> y almacena en datos_emp
                    datos_emp[dt.get_text(strip=True)] = dd.get_text(strip=True)

        print("datos_emp devuelve: " + str(datos_emp))
        return datos_emp
    
    def recopilarDatos_VersionChatGPT_Mateo(self):
        # Encuentra todos los elementos <dl>
        lsdl = self.driver.find_elements(By.XPATH, '//dl')

        lsdl_soup = []

        # transforma cada dl, uno por uno. (no se puede hacer sobre todos directamente)
        for dl in lsdl:
            # lista de bloques con etiqueta dl transformada a soup.
            dl_soup = BeautifulSoup(dl.get_attribute("outerHTML"), "html.parser")
            lsdl_soup.append(dl_soup) 

        datos_emp = {}  # Diccionario para almacenar los datos
        lssdd = []

        for dl in lsdl_soup: # Itera sobre cada elemento <dl> dl -> dt / dt
            lsdt = dl.find_all('dt')
            for dt in lsdt: 
                lsdd = []
                if dt:
                    dt_y_dd = dt.find_next_siblings()
                    for element in dt_y_dd: 
                        if element.name == 'dd':
                            lsdd.append(element) 
                        else:   
                            lssdd.append(lsdd)
                            break              

                # for dt, dd in zip(ls_dt, ls_dd): # Itera sobre los elementos <dt> y <dd> y almacena en datos_emp
                #    datos_emp[dt.get_text(strip=True)] = dd.get_text(strip=True)

        print("Datos recopilados:") # Imprime los resultados
        for clave, valor in datos_emp.items():
            print(f"{clave}: {valor}")

        # Supongamos que tienes un objeto BeautifulSoup llamado soup que contiene tu HTML


    
    