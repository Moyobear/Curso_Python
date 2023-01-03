class Vehiculo:
    color = 'Rojo'
    ruedas = 4
    puertas = 5


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 6


newCoche = Coche()
print(dir(newCoche))
