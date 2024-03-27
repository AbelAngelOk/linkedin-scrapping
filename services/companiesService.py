from services.commonService import CommonService
from constants.companiesConstants import CompaniesConstants
from bs4 import BeautifulSoup
import time

class CompaniesService(CommonService):

    def __init__(self, driver):
      super().__init__(driver)
      self.Constants = CompaniesConstants(driver)
   
    def obtenerListaDeEmpresas(self):
        ''' obtiene la lista de empresas de la pagina '''
        cant_elements = len( self.WaitAndFindElements( self.Constants.cant_empresas() ) ) # guarda la cantidad de empresas    
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);") # scrolea hacia el final de la pagina
        time.sleep(2) # espera 3 segundos
        new_cant_elemets = len(self.WaitAndFindElements( self.Constants.cant_empresas() )) # guarda la cantidad de empresas despues de scrolear

        while cant_elements != new_cant_elemets: # si la cantidad es distintas despues del scroll entonces repetir el proceso.
            cant_elements = new_cant_elemets
            self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);") 
            time.sleep(2)
            new_cant_elemets = len(self.WaitAndFindElements( self.Constants.cant_empresas() ))

        print(f'cantidad de empresas listadas: {cant_elements} ({new_cant_elemets})')
        try:
            lista_empresas = self.WaitAndFindElements( self.Constants.cant_empresas() )
            if (len(lista_empresas) == 0):
                print("Error al obtener la lista de empresas")
        except:
            print("Error al obtener la lista de empresas")

        return lista_empresas

    def extraerInformacionBasicaDeEmpresa(self, html_empresas):
        ''' desde la pagina de listados de empresas, retorna el nombre y seguidores de la empresa pedida'''
        soup = BeautifulSoup(html_empresas, "html.parser") # Crear un objeto BeautifulSoup para facilitar el análisis del HTML
        nombre_empresa = soup.find("span", class_="entity-result__title-text").get_text(strip=True) # Obtener el nombre de la empresa
        seguidores_empresa = soup.find("span", class_="member-insights__reason").get_text(strip=True) # Obtener el número de seguidores de la empresa   

        datos_empresa = {}

        datos_empresa["Nombre"] = nombre_empresa
        datos_empresa["Seguidores"] = seguidores_empresa

        return datos_empresa
        
    def GetEnlaceEmpresa(self, html_empresas):
        ''' retorna el enlace a la pagina linkedin de la empresa '''
        soup = BeautifulSoup(html_empresas, "html.parser") # Crear un objeto BeautifulSoup para facilitar el análisis del HTML
        enlace = soup.find("a", class_="app-aware-link")  # Obtener el enlace a la empresa
        return enlace.get("href") # Extraer el valor del enlace

    def extraerNombreDeLaEmpresa(self, html_empresas):
        ''' desde la pagina de listados de empresas, retorna el nombre y seguidores de la empresa pedida'''
        soup = BeautifulSoup(html_empresas, "html.parser") # Crear un objeto BeautifulSoup para facilitar el análisis del HTML
        return soup.find("span", class_="entity-result__title-text").get_text(strip=True) # Obtener el nombre de la empresa



