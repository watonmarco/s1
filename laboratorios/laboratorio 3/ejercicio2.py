a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]

# a
d = a + b + c
print(d,"Listas concatenadas")

# b
d.insert(-1,20)
print(d,"Lista con el numero 20 en la penultima posicion")

# c
d.sort(reverse=True)
print(d,"Lista ordenada de forma descendente")

# d
e = [4,5,6]
d = d + e
print(d,"Lista + [4,5,6] al final")

# e
total = sum(d)
print("Suma de todos los numeros de la lista: ",total)

#f
cuenta = len(d)
promedio = total / cuenta
print(f"promedio: {promedio:.0f}")      # promedio simple = sin decimales ??