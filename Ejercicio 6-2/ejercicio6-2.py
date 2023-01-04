# Inicio de nuestro Programa:

# Clase Alumno:
class Alumno:
    nombre = None
    nota = None

    # Constructor de la clase:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    # Imprimimos los valores:
    def getAtributos(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    # Devolvemos el resultado final:
    def resultadoFinal(self):
        if self.nota > 0 and self.nota < 10:
            print('El alumno ha sido reprobado')
        else:
            print('El alumno fue aprobado')


# Instanciamos la clase y creamos Alumnos:
a1 = Alumno("Alberto", 16)
a2 = Alumno("Gustavo", 8)
a3 = Alumno("Ismael", 19)
a4 = Alumno("Jonathan", 20)

# Obtenemos los atributos:
a1.getAtributos()
a2.getAtributos()
a3.getAtributos()
a4.getAtributos()

# Resultado Final:
a1.resultadoFinal()
a2.resultadoFinal()
a3.resultadoFinal()
a4.resultadoFinal()
