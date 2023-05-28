import random

num = []

for i in range(20):
    num.append(random.randrange(40,350))
print(num)

busca = input("Ingrese el número que quiera buscar: ")

rep = num.count(int(busca))
if rep > 1:
    print(f"el número {busca} se repite {rep} veces")
else:
    print(f"el número {busca} se repite {rep} vez")