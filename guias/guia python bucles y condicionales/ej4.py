print("Propiedad descubierta por Nicómaco de Gerasa")
print("1^3 = 1 = 1")
print("2^3 = 3 + 5 = 8")
print("3^3 = 7 + 9 + 11 = 27")

num = int(input("Ingrese una cantidad de cubos para aplicar la propiedad: "))
a = 1
b = 1
lista = []

for cubo in range(1, num + 1):
    b = b + (cubo * 2)

    lista = [impar for impar in range(a, b, 2)]
    impares = " + ".join(map(str, lista))

    suma = sum(lista)
    print(f"{cubo}^3 = {impares} = {suma}")

    a = b
# hola