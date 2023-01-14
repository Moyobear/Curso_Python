lista = input("Por favor introduce varios países separados por coma:\n")

paises = [pais for pais in lista.split(",")]

print(",".join(sorted(list(set(paises)))))
