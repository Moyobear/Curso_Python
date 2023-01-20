import sqlite3

conn = sqlite3.connect('ejercicio.db')
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO alumnos(id, nombre, apellido) VALUES(1, 'Jonathan', 'Rodriguez')")
cursor.execute(
    "INSERT INTO alumnos(id, nombre, apellido) VALUES(2, 'Orion', 'Martinez')")
cursor.execute(
    "INSERT INTO alumnos(id, nombre, apellido) VALUES(3, 'Omar', 'Quintana')")
cursor.execute(
    "INSERT INTO alumnos(id, nombre, apellido) VALUES(4, 'Simón', 'Atencio')")
cursor.execute(
    "INSERT INTO alumnos(id, nombre, apellido) VALUES(5, 'David', 'Martínez')")
cursor.execute(
    "INSERT INTO alumnos(id, nombre, apellido) VALUES(6, 'Alexander', 'Rodriguez')")
cursor.execute(
    "INSERT INTO alumnos(id, nombre, apellido) VALUES(7, 'Carmen', 'Herrera')")
cursor.execute(
    "INSERT INTO alumnos(id, nombre, apellido) VALUES(8, 'José', 'Izquiel')")

conn.commit()
rows = cursor.execute('SELECT * FROM alumnos WHERE nombre="Orion"')
data = rows.fetchone()
print(data)

cursor.close()
conn.close()
