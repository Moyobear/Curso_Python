import calendar


def consularBiciesto():
    year = int(input("Consulta si un año es Biciesto o no => "))

    if calendar.isleap(year):
        print(f"El año {year} es Biciesto")
    else:
        print(f"El año {year} no es biciesto")


consularBiciesto()
