# solicitámos el peso:
peso = float(input('indique su peso en kilogramos '))

# solicitámos la altura:
altura = float(input('indique su altura en metros '))

# calculámos el IMC:
indice = round(peso / altura ** 2, 2)

# devolvemos el resultado:
if indice < 18.5:
    print('Tu índice de masa corporal es: ' +
          str(indice) + ', además indica PESO BAJO!')
elif indice >= 18.6 and indice < 24.9:
    print('Tu índice de masa corporal es: ' +
          str(indice) + ', además indica PESO NORMAL!')
elif indice >= 25.0 and indice < 29.9:
    print('Tu índice de masa corporal es: ' +
          str(indice) + ', además indica SOBREPESO!')
elif indice > 30:
    print('Tu índice de masa corporal es: ' +
          str(indice) + ', además indica OBESIDAD!')
