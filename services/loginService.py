from selenium.common.exceptions import NoSuchElementException 
from constants.loginConstants import LoginConstants
from services.commonService import CommonService

class AntiBotException(Exception):
    pass

class DatosIncorrectosException(Exception):
   pass

class LoginService(CommonService):
    ''' servicio para iniciar sesion '''
    
    def __init__(self, driver):
      super().__init__(driver)
      self.Tuple = LoginConstants(driver)
      
    def login(self, email:str, password:str):
        ''' inicia sesion con un email y password '''
        try:        
          print(f'email: {email}')
          print(f'password: {password}')
          self.WaitAndSendKeys(self.Tuple.txt_username(), email) # self.Locator.txt_username().send_keys(email)        
          self.WaitAndSendKeys(self.Tuple.txt_password_field(), password) # self.Locator.txt_password_field().send_keys(password)
          self.WaitAndClick(self.Tuple.btn_submit()) # self.Locator.btn_submit().click()
                 
        except NoSuchElementException as e:
          print("SE ENCONTRO UN ERROR AL INICIAR SESION: ", e)
          raise Exception("Se encontro un error al iniciar sesion")

        if ( self.isPresent( self.Tuple.human_verification() ) or self.isPresent( self.Tuple.email_verification() )):
          print("LA PAGINA ACTIVO LA SEGURIDAD ANTI BOT")
          raise AntiBotException("La página ha activado la seguridad anti-bot")

        if ( self.Tuple.isVisible( self.Tuple.alert() ) ):
          print("ERROR EN USUARIO O PASSWORD INGRESADO")
          raise DatosIncorrectosException("Email o password incorrecto")


