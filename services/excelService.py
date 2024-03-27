import pandas as pd

class ExcelService():
    def __init__(self) -> None:
        self.excelId = ""

    def createExcel(self, lista_empresas, excelAutoName=True):
        if len(lista_empresas) == 0: 
            return
        if not excelAutoName:
            nombre_excel = input("¿Qué nombre desea darle al archivo? (Pulsa Enter para 'datos_empresas', aunque si ya tienes uno con ese nombre no generará otro) ")
            print("Generando Excel...")
            if not nombre_excel:
                nombre_excel = 'datos_empresas'
        else:
            nombre_excel = 'datos_empresas'
        df_empresas = pd.DataFrame(lista_empresas)
        nombre_excel_con_extension = nombre_excel + '.xlsx'
        self.excelId = nombre_excel_con_extension
        df_empresas.to_excel(nombre_excel_con_extension, index=False)
        print(f"Datos exportados exitosamente a {str(nombre_excel_con_extension)}")

    def getExcelIdCreated(self):
        return self.excelId
        
        
        