from flask import request
from services.loginService import LoginService
from services.companiesService import CompaniesService
from services.companyService import CompanyService
from Context import Context
from services.excelService import ExcelService
from services.filtersService import FiltersService

class Scrapper(Context): 

    def __init__(self, handlessMode=True, excelAutoName=True, seleccionarDatos=True):        
        super().__init__(handlessMode)
        self.empresas_data = []
        self.excelAutoName = excelAutoName
        self.seleccionarDatos = seleccionarDatos

    def run(self, email:str, password:str): 
        companies_service = CompaniesService(self.driver) 
        self.ingresarLinkedin(email, password)
        lista_empresas = companies_service.obtenerListaDeEmpresas()
        self.agregarDatosPorCadaEmpresa(lista_empresas)
        return self.gestionarDatos()
    
    def ingresarLinkedin(self, email:str, password:str):
        login_service = LoginService(self.driver)
        self.driver.get(self.BASE_URL) # iniciar_chrome.
        login_service.login(email, password) # inicia sesion con los datos de context
        self.driver.get(self.MY_NETWORK_URL) # redireccion a la pagina de la variable de context

    def agregarDatosPorCadaEmpresa(self, lista_empresas):
        for _ , empresa in enumerate(lista_empresas):
            datos_empresa = self.recopilarDatosDeLaEmpresa(empresa)
            self.empresas_data.append(datos_empresa)
        print("los datos finales son: " + str(self.empresas_data) )

    def recopilarDatosDeLaEmpresa(self, empresa):
        ''' recopila datos de cada empresa y los guarda en "empresas_data" '''
        companies_service = CompaniesService(self.driver)
        company_service = CompanyService(self.driver)
        empresa_data = {}

        empresa_html = empresa.get_attribute("outerHTML")
        empresa_data.update( companies_service.extraerInformacionBasicaDeEmpresa(empresa_html) )
        company_service.AbrirNuevaVentanaCon( companies_service.GetEnlaceEmpresa(empresa_html) ) 

        # if (company_service.IrAcercaDe() ):
        try:
            datos_de_acerca_de = company_service.recopilarDatos_VersionChatGPT()
            empresa_data.update(datos_de_acerca_de)
        except Exception as e:
            print("error en 'acerca de' de la empresa: " + str(companies_service.extraerNombreDeLaEmpresa(empresa_html)))

        company_service.cerrarVentana()
        return empresa_data

    def gestionarDatos(self):
        excel_service = ExcelService()
        filters_service = FiltersService()

        datos_a_exportar = filters_service.filtrar_datos_flask(self.empresas_data, request.args.to_dict() ) if self.seleccionarDatos else self.empresas_data
        excel_service.createExcel(datos_a_exportar, self.excelAutoName)
        return excel_service.getExcelIdCreated()    