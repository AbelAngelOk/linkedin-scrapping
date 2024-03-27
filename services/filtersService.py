class FiltersService:
    def __init__(self):
        # Crea un diccionario de opciones disponibles. La clave es el número de la opción y el valor es el nombre de la opción.
        # El nombre tiene que estar igual a cómo se encuentra en linkedin ya que con eso se hace el filtro.
        self.opciones_disponibles = {"1": "Nombre", "2": "Sitio web", "3": "Teléfono", "4": "Tamaño de la empresa", "5": "Seguidores", "6": "Sector", "7": "Especialidades", "8": "Sede", "9": "Fundación"}
        self.filtros_elegidos = [] # Crea un conjunto vacío para almacenar los filtros elegidos por el usuario.
        self.lista_empresas_filtradas = []
        
    def elegir_filtros(self):
        ''' Elige los filtros que desea usar el usuario para filtrar las empresas. '''
        # Bucle creado para poder utilizar break y continue
        while True:
            print("Elige los datos que quieres obtener de cada empresa (tipeá los números):")

            # Crea un diccionario de opciones filtradas excluyendo aquellas que ya han sido seleccionadas como filtros.
            opciones_filtradas = {key: value for key, value in self.opciones_disponibles.items() if value not in self.filtros_elegidos}

            for key, value in opciones_filtradas.items():
                print(f"{key}. {value}") # Imprime la lista de opciones filtradas

            print("0. Finalizar\n")
            print("Palabras elegidas:", self.filtros_elegidos)

            filtros_usuario = input("Ingresa el filtro deseado: ") # Pide al usuario que ingrese el filtro

            if filtros_usuario in opciones_filtradas: # Verifica si la opción elegida por el usuario está en las opciones disponibles para filtrar.
                palabra_elegida = opciones_filtradas[filtros_usuario]

                if palabra_elegida in self.filtros_elegidos: # Si está presente, determina si esa opción ya ha sido seleccionada anteriormente como filtro.
                    self.filtros_elegidos.remove(palabra_elegida) # Si la opción ya está en los filtros elegidos, se elimina de la lista de filtros.
                    print(f"Se quitó '{str(palabra_elegida)}' de la lista.")
                else:
                    self.filtros_elegidos.append(palabra_elegida) # Si la opción no está en los filtros elegidos, se agrega a la lista de filtros.
                    print(f"Se agregó '{str(palabra_elegida)}' a la lista.")

            elif filtros_usuario == "0": # Si el usuario ingresa el número 0, termina el programa de filtros.
                print("Finalizando...")
                break
            else:
                print("Opción no válida. Por favor, elige un número del 1 al 9.")
                continue
        
    def filtrar_datos(self, empresas_a_filtrar):
        """ Filtra las empresas según los filtros elegidos por el usuario. """
        self.elegir_filtros() # Llama a la función elegir_filtros() para elegir los filtros que desee el usuario.
        for empresa in empresas_a_filtrar: # Itera sobre cada empresa en la lista de empresas a filtrar.
            resultado_filtrado = {dato: empresa.get(dato, "No disponible") for dato in self.filtros_elegidos} # Crea un diccionario con los datos filtrados de la empresa. Si el dato no existe, se establece como "No disponible".
            self.lista_empresas_filtradas.append(resultado_filtrado) # Agrega el diccionario filtrado a la lista de empresas filtradas.
        return self.lista_empresas_filtradas

    def filtrar_datos_flask(self, empresas_a_filtrar, parametros):
        """ Filtra las empresas según los filtros elegidos por el usuario. """
        # self.elegir_filtros(parametros) # Llama a la función elegir_filtros() para elegir los filtros que desee el usuario.
        filtros_elegidos = {clave: valor for clave, valor in parametros.items() if valor == "true"}
        for empresa in empresas_a_filtrar: # Itera sobre cada empresa en la lista de empresas a filtrar.
            resultado_filtrado = {dato: empresa.get(dato, "No disponible") for dato in filtros_elegidos} # Crea un diccionario con los datos filtrados de la empresa. Si el dato no existe, se establece como "No disponible".
            self.lista_empresas_filtradas.append(resultado_filtrado) # Agrega el diccionario filtrado a la lista de empresas filtradas.
        return self.lista_empresas_filtradas
                