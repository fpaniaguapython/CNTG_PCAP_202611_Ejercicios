from enum import Enum

class LogType(Enum):
    FILE = 1
    DATABASE = 2
    WEBSERVICE = 3

# Este closure es un generador de funciones configuradas con distintas alternativas
def logger_factory(log_type: LogType):
    def logger(log: str):
        match log_type:
            case LogType.FILE:
                print(f'Escribiendo el log {log} en fichero')
            case LogType.DATABASE:
                print(f'Escribiendo el log {log} en base de datos')
            case LogType.WEBSERVICE:
                print(f'Escribiendo el log {log} en un web service')
    return logger

logger_fichero = logger_factory(LogType.FILE)
logger_ws = logger_factory(LogType.WEBSERVICE)

logger_fichero('Ha ocurrido un error en el acceso')

logger_ws('Ha ocurrido un error en la validación')