ingresar = int(input("indique la cantidad de numeros que va a ingresar: "))
lista = []
for i in range(ingresar):
    num = input(f"ingrese su {i + 1}° numero: ")
    lista.append(num)
print(lista)

def sumat():
    total = 0
    for i in range(ingresar):
        total += int(lista[i])
    return total
print(f"la suma total es: {sumat()}")

def sumap():
    total = 0
    pares = []
    for i in range(ingresar):
        if int(lista[i]) % 2 == 0:
            pares.append(lista[i])
        if int(lista[i]) % 2 != 0:
            pares.append(0)
        total += int(pares[i])
    return total
print(f"la suma de los pares es: {sumap()}")

def sumai():
    total = 0
    impares = []
    for i in range(ingresar):
        if int(lista[i]) % 2 != 0:
            impares.append(lista[i])
        if int(lista[i]) % 2 == 0:
            impares.append(0)
        total += int(impares[i])
    return total
print(f"la suma de los impares es: {sumai()}")