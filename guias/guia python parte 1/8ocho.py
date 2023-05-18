mes = input("Ingrese un mes: ")

if mes in ("Enero","Febrero","Marzo"):
    print(f" {mes} pertenece a la estación de: Verano")
elif mes in ("Abril","Mayo","Junio"):
    print(f" {mes} pertenece a la estación de: Otoño")
elif mes in ("Julio","Agosto","Septiembre"):
    print(f" {mes} pertenece a la estación de: Invierno")
elif mes in ("Octubre","Noviembre","Diciembre"):
    print(f" {mes} pertenece a la estación de: Primavera")