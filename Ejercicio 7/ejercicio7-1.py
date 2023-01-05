# Importamos calculadora:
from calculadora import *

a, b, c, d = (15, 30, 26, 4)

print("{} + {} = {}".format(a, b, suma(a, b)))
print("{} - {} = {}".format(b, d, resta(b, d)))
print("{} * {} = {}".format(b, b, multiplica(b, b)))
print("{} / {} = {}".format(a, c, divide(a, c)))
