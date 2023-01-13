f = open('ficheroEjercicio8.txt', 'w')
f.write('Esta es la primera linea del fichero del ejercicio 8 \n')
f.write('Esta es la segunda linea del fichero del ejercicio 8 \n')
f.close()

f = open('ficheroEjercicio8.txt', 'r+')
f.readline()
f.write('Esta es la tercera linea del fichero del ejercicio 8 \n')
f.write('Esta es la cuarta linea del fichero del ejercicio 8 \n')

f.seek(0)
print(f.read())
f.close()
