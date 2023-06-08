def chayanne():
    nombres = []
    while True:
        nombre = input('ingrese un nombre ("1" para dejar de preguntar): ')
        nombres.append(nombre)
        if nombre == "1":
            break
    nombres.pop(-1)
    return nombres
lista = chayanne()

def luis_miguel():
    cuenta = 0
    for i in range(len(lista)):
        c_nombre = len(lista[i])
        cuenta += c_nombre
    return cuenta
cuenta = luis_miguel()

def ricardo_arjona():
    print(lista)
    print(f"el total de letras contadas es de: {cuenta}")
ricardo_arjona()