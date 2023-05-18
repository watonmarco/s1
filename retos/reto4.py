### -> cosas que me faltaron o que podria poner

### print("Ingrese los datos del primer paciente")
nombre1 = str(input("Nombre del primer paciente: "))    ### str(input("Nombre: ")) noma
peso1 = float(input("Peso: "))                          ### podria ponerle restricciones igual
estatura1 = int(input("Estatura (en centímetros): "))   ### podria ponerle restricciones igual
edad1 = int(input("Edad: "))
while edad1 < 0:    ### while edad1 < 0 or edad1 > 140: ### while not edad1.isdigit() -> solo admite digitos
    print("La edad ingresada no es válida, ingrésela nuevamente")
    edad1 = int(input("Edad: "))
    ### break   ->  para romper el bucle
### print("\n")

nombre2 = str(input("Nombre del segundo paciente: "))
peso2 = float(input("Peso: "))
estatura2 = int(input("Estatura (en centímetros): "))
edad2 = int(input("Edad: "))
while edad2 < 0:
    print("La edad ingresada no es válida, ingrésela nuevamente")
    edad2 = int(input("Edad: "))

nombre3 = str(input("Nombre del tercer paciente: "))
peso3 = float(input("Peso: "))
estatura3 = int(input("Estatura (en centímetros): "))
edad3 = int(input("Edad: "))
while edad3 < 0:
    print("La edad ingresada no es válida, ingrésela nuevamente")
    edad3 = int(input("Edad: "))

t_paciente1 = nombre1,peso1,estatura1,edad1
t_paciente2 = nombre2,peso2,estatura2,edad2
t_paciente3 = nombre3,peso3,estatura3,edad3

t_pacientes = t_paciente1,t_paciente2,t_paciente3       # esto era opcional
print(t_pacientes)


# for i in range(3):
#    nombre = input("nombre {}: format")