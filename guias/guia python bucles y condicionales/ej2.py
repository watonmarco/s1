a = 500
b = 456
fin = 800
suma = 0
aa = 10
bb = 2

while a < fin:
    suma = suma + a + b
    a = a + aa
    b = b - bb
else:
    suma = suma + fin
print(f"La suma total es: {suma}")