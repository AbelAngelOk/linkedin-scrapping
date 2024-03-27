from HandleDriver import HandleDriver

class Context():
    
    def __init__(self, handlessMode):
        self.BASE_URL = "https://www.linkedin.com/login/es"
        self.MY_NETWORK_URL = "https://www.linkedin.com/mynetwork/network-manager/company/"
        self.EMAIL =  "abel.angel96@outlook.es" # "mateocao@hotmail.com" 
        self.PSWRD =  "TrabajosIt2023" # "Villavicencio23" 

        self.handle_driver = HandleDriver()
        self.handle_driver.initialize_driver(headless=handlessMode)
        self.driver = self.handle_driver.get_driver()
