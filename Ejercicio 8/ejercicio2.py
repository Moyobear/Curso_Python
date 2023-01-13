import pickle


class Vehiculo:
    marca = ''
    anio = 0
    puertas = 0
    tipoMotor = 'gas'
    color = 'blanco'

    def __init__(self, marca, anio, puertas, tipoMotor, color):
        self.marca = marca
        self.anio = anio
        self.puertas = puertas
        self.tipoMotor = tipoMotor
        self.color = color

    def getCaracteristicas(self):
        return f'Este Vehiculo es marca {self.marca}, es año {self.anio}, tiene {self.puertas} puertas, su motor es de combustible a {self.tipoMotor}, y su color es {self.color}'


carro1 = Vehiculo('Chevrolet', 2018, 5, 'gasolina', 'blanco')

# print(carro1.getCaracteristicas())

# *serialzando:
# f = open('datosVehiculo.bin', 'wb')
# pickle.dump(carro1, f)
# f.close()

# *desserializando:
f = open('datosVehiculo.bin', 'rb')
carro1 = pickle.load(f)
f.close()

print(carro1.getCaracteristicas())
