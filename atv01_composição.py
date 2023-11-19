class Motor:
    def __init__ (self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor(potencia=100)
        print (f"Carro {modelo} tem a potencia de: {self.motor.potencia}")

carro1 = Carro("Gol")