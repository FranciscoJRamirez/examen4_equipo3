import abc

class Vehiculo(abc.ABC):
    def __init__(self, placa, marca, color):
        self.placa = placa
        self.marca = marca
        self.color = color
    @abc.abstractmethod
    def apaga(self):
        pass
    @abc.abstractmethod
    def enciende(self):
        pass
class Camion(Vehiculo):
    esta_encendido=False
    def enciende(self):
        if self.esta_encendido:
            return("Esta encendido")
        else:
            return self.apaga()
    def apaga():
        return "Esta apagado"
    def prenderApagar():
        if self.esta_encendido:
            self.esta_encendido = False
        else:
            self.esta_encendido = True

class Coche():
    esta_encendido=False
    def enciende(self):
        if self.esta_encendido:
            return("Esta encendido")
        else:
            return self.apaga()
    def apaga():
        return "Esta apagado"
    def prenderApagar():
        if self.esta_encendido:
            self.esta_encendido = False
        else:
            self.esta_encendido = True

