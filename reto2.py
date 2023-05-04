diccionario = {
    "Nombre del estudiante":"",
    "Nombre de la asignatura":"",
    "Nota laboratorio 1":"",
    "Nota laboratorio 2":"",
    "Promedio ponderado":""
}

diccionario["Nombre del estudiante"] = input("nombre del estudiante: ")
diccionario["Nombre de la asignatura"] = input("nombre de la asignatura: ")
diccionario["Nota laboratorio 1"] = input("nota laboratorio 1: ")
diccionario["Nota laboratorio 2"] = input("nota laboratorio 2: ")

ponderado = float(diccionario["Nota laboratorio 1"]) * 0.3 + float(diccionario["Nota laboratorio 2"]) * 0.7

diccionario["Promedio ponderado"] = f"{ponderado:.1f}"

print(diccionario)

## la solucion era diferente xd pero igual sirve