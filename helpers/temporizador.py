import time

class Temporizador:

    def __init__(self):
        self.start_time = 0

    def start(self):
        """Inicia el tiempo de ejecución para ver cuánto tarda en ejecutarse el programa"""
        self.start_time = time.time() 

    def end(self):
        execution_time = time.time() - self.start_time
        if execution_time < 60:
            print("El programa tardó:", execution_time, "segundos en ejecutarse.")
        else:
            minutes = int(execution_time // 60)
            seconds = int(execution_time % 60)
            print("El programa tardó:", minutes, "minutos y", seconds, "segundos en ejecutarse.")