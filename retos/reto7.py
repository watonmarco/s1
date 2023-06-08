def funcion():
    cuenta = {}

    frase = input("Ingrese una frase: ")
    palabras = frase.split(" ")

    for i in palabras:
        cantidad = len(i)
        cuenta[i] = cantidad
    return cuenta
# si

diccionario = funcion()
print(diccionario)