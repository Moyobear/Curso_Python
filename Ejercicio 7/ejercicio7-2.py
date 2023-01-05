import time

horaLocal = time.strftime('%H')
minutoLocal = time.strftime('%M')

print("Recoge y largate que son más de las 7!") if int(horaLocal) >= 19 else print(
    "Quedan {} horas y {} minutos para largarte".format(18 - int(horaLocal), 59-int(minutoLocal)))
