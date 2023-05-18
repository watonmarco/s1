a = int(input("Ingrese medida del primer lado: "))
b = int(input("Ingrese medida del segundo lado: "))
c = int(input("Ingrese medida del tercer lado: "))

if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    print("Es isósceles")
elif a == b == c:
    print("Es equilátero")
else:
    print("Es escaleno")

import math

p = (a + b + c)
s = p / 2
area = math.sqrt(s*(s - a)*(s - b)*(s - c))

print(area)