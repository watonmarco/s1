parrafo = ("La Universidad de los Lagos es una institución estatal fundada en 1993. Esta universidad regional entrega una contribución significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación democrática.")
palabras = parrafo.split()

ucount = parrafo.count("universidad")
Ucount = parrafo.count("Universidad")
uUcount = ucount + Ucount
print(f'La palabra "universidad" se repite {uUcount} veces durante el párrafo')

utuple = list()
for i in range(len(palabras)):
    if palabras[i] == "universidad" or palabras[i] == "Universidad":
        utuple.append(palabras[i])
utuple = tuple(utuple)
print(utuple)