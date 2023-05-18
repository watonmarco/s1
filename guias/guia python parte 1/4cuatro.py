nombre1 = input("Ingrese su nombre: ")
nombre2 = input("Ingrese otro nombre: ")

n1 = list(nombre1)
n2 = list(nombre2)

if n1[0] == n2[0]:
    print("Comienzan con la misma letra")
elif n1[-1] == n2[-1]:
    print("Terminan con la misma letra")
elif n1[0] == n2[0] and n1[-1] == n2[-1]:
    print("Comienzan y terminan con la misma letra")
else:
    print("No comienzan ni terminan con la misma letra")