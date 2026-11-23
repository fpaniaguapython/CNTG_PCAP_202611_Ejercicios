class Motor:
    def __init__(self, fabricante: str, 
                 modelo: str, cilindrada: float, consumo_medio: float):
        self.fabricante = fabricante
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.consumo_medio = consumo_medio
        self.rpm = 0

    def acelerar(self, cantidad=10):
        #self.rpm = self.rpm + cantidad # La línea siguente es equivalente a esta
        self.rpm+=cantidad

    def desacelerar(self, cantidad=10):
        # self.rpm = self.rpm - cantidad # La línea siguente es equivalente a esta
        self.rpm-=cantidad


# Instanciación o creación del objeto o instancia
motor_1 = Motor(fabricante='Toyota', 
                modelo='VVT-i', cilindrada=1.8, consumo_medio=6.5)
motor_2 = Motor('Honda', 'i-VTEC', 2.0, 7.2)

# Llamadas a los métodos de acelerar y desacelerar
motor_1.acelerar(cantidad=10)
motor_1.acelerar(cantidad=10)
motor_1.acelerar(cantidad=10)
print(motor_1.rpm)