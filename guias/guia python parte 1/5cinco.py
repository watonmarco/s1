while True:
    Lab1 = int(input("Ingrese nota de laboratorio 1: "))
    if Lab1 < 1 or Lab1 > 7:
        print("Ingrese una nota válida")
        continue
    else:
        break

while True:
    Lab2 = int(input("Ingrese nota de laboratorio 2: "))
    if Lab2 < 1 or Lab2 > 7:
        print("Ingrese una nota válida")
        continue
    else:
        break

while True:
    Lab3 = int(input("Ingrese nota de laboratorio 3: "))
    if Lab3 < 1 or Lab3 > 7:
        print("Ingrese una nota válida")
        continue
    else:
        break

ponderado = Lab1 * 0.3 + Lab2 * 0.4 + Lab3 * 0.3
print(ponderado)