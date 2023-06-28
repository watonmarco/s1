trabajadores = [["Juan",[700000,650000,690000]],
                ["María",[681000,710000,590000]],
                ["Pedro",[590000,635000,705000]]]

# A
def promedio(trabajador):
    suma = sum(trabajadores[trabajador][1])     # esto lo escribimos al reves en el papel
    sueldos = len(trabajadores[trabajador][1])
    promedio = suma / sueldos
    return round(promedio,2)    # habíamos puesto (promedio,3) pero pedian 2 decimales y no 3

# B
def mas_alto(trabajador):
    maximo = max(trabajadores[trabajador][1])   # esto lo escribimos al reves en el papel
    return maximo

# C
def impuestos(sueldo):  # se nos olvidó poner un parámetro
    r_impuestos = sueldo*0.1225     # teníamos r_impuestos = maximo*0,1225 pero la variable maximo no existe, y en los decimales se usa punto y no coma
    s = sueldo - r_impuestos        # teníamos s = sueldo - r_impuestos pero la variable maximo no existe
    return s

# D     no recuerdo por que lo hicimos tan pobre, creo que por falta de tiempo o no se
'''for trabajador in range(0,3):
    print(promedio(trabajador))
    print(mas_alto(trabajador))
    print(impuestos(mas_alto(trabajador)))  # teníamos print(impuestos(trabajador))'''

#   creo que debió ser así
for trabajador in range(0,3):
    nombre = trabajadores[trabajador][0]
    sueldo = trabajadores[trabajador][1]
    print("Nombre:",nombre)
    print("Lista de sueldos:",sueldo)
    print("Promedio de sueldo:")
    print(promedio(trabajador))
    print("Sueldo más alto:")
    print(mas_alto(trabajador))
    print("Sueldo más alto con el 12,25% de impuestos: ")
    print(impuestos(mas_alto(trabajador)))
    print("\n")