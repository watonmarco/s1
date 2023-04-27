#1. operadores aritmeticos
a = 20
b = 10
c = 90
d = 35

print("suma entre a y c: ", a + c)
print("resta entre a y b: ", a - b)
print("multiplicacion de b y d: ", b * d)
print("b dividido en d ", b / d)
print("d elevado a b: ", d ** b)
print("algo: ", d // b)

t = 6
g = 9.81
v = g * t
print(f"la velocidad del objeto en caida libre es de: {v} m/s")

## diferentes manear de formatear un float, la segunda se ve poderosa
print("la velocidad del objeto en caida libre es de: {:.2f}".format(v),"m/s")
print(f"la velocidad del objeto en caida libre es de: {v:.2f} m/s")

c1 = 4 + 3
print(type(c1))

c2 = complex(3, -5)
print("el numero complejo es: ",c2)
print(c2.real)
print(c2.imag)

print("hola" * 3)                   # impresionante, se puede multiplicar texto
### print("hola" * 3.5 * 2)                 # esto no se puede
print("hola" * (int((10 * 2) / 5)))         # esto si
print("\n")

#2. comparadores
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print("\n")

animal_domestico = "gato"
animal_salvaje = "leopardo"

print(animal_domestico == animal_salvaje)
print(animal_domestico != animal_salvaje)
print(animal_domestico > animal_salvaje)
print(animal_domestico < animal_salvaje)
print(animal_domestico >= animal_salvaje)
print(animal_domestico <= animal_salvaje)
print("\n")