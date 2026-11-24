class Motor:
    def __init__(self, nombre, potencia):
        # self.nombre = nombre # Dificultad de acceso al nombre de Motor
        self.__nombre = nombre
        self.potencia = potencia

class MotorElectrico(Motor):
    def __init__(self, nombre_motor, nombre_electrico, potencia):
        super().__init__(nombre=nombre_motor, potencia=potencia)
        # self.nombre = nombre_electrico # Dificultad de acceso al nombre de Motor
        self.__nombre = nombre_electrico

motor_electrico = MotorElectrico('Motor V8', 'Motor 120w', 100)

print(motor_electrico.potencia)
# print(motor_electrico.nombre) # Imposibilidad de acceso al nombre de Motor
print(motor_electrico._MotorElectrico__nombre) # Motor 120w
print(motor_electrico._Motor__nombre) # Motor V8