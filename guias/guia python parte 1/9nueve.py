numeros = [4,3,8,12,6,10,14,3,6]
print(numeros)

# a
numeros.pop(-1)
print(numeros)

# b
numeros.insert(0,2)
print(numeros)

# c
for i in range(15):
    if numeros.count(i) >= 2:
        numeros.remove(i)
        break
print(numeros)
print("\n")

# d
numeros = [4,3,8,12,6,10,14,3,6]
print(numeros)
suma = sum(numeros)
cuenta = len(numeros)
media = suma / cuenta
print(f"media: {media:.2f}")

numeros.sort()          # ordeno la lista
print(numeros)          # la imprimo
mediana = cuenta / 2
print(f"mediana: {numeros[int(mediana)]}")