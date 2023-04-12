#1. datos de tipo numérico
estatura = 1.71
peso = 70
complejo = 1 + 4j

print("Impresión del número complejo:",complejo)

## operacíón aritmética básica
imc = peso/(estatura*estatura)
print("mi imc es de:",imc)
print("mi imc es de: {:.2f}" .format(imc)) #formateo, para redondear decimales
print("\n")

#2. datos de tipo cadena de caracteres
asignatura = "Programación"
carrera = "Ingeniería Civil en Informática"

## hola (saludo)
print("Hola, soy estudiante de la carrera de",carrera,"y estoy en clase de",asignatura+", un (1) cordial saludo")
print(f"Hola, soy estudiante de la carrera de {carrera} y estoy en clase de {asignatura}, un (1) cordial saludo")

print(f"La cantidad de caracteres que tiene {carrera} es de: ", len(carrera)) #len -> variable que cuenta caracteres
print("\n")

#3. valores booleanos (no se que es un booleano)
ampolleta = False
interruptor = True

print(type(ampolleta))
print(type(imc))
print(type(carrera))
print(type(peso))
print("\n")

#4. datos de tipo array (o arreglos)
estudiantes = ("Matías", "Marco", "Cristóbal", "Sebastian")
num = (1,2,3,4,5,6)
lenguaje = ("Python")
print(estudiantes)
print(num)
print(lenguaje)

## listas
nueva_lista = list()
print("esta es una lista vacía",nueva_lista)
print("la cantidad de datos en esta lista es:",len(nueva_lista))

otra_lista = list()
print("esta es otra lista varía",otra_lista)
print(type(otra_lista))

## lista compuesta
compuesta = [1,"Marco",True,100,"Arroz","Marco"]
codigo,minombre,estado,peso,comida,minombre = compuesta
print(compuesta)

print("esta es una lista compuesta",compuesta)
print("hay",len(compuesta),"datos en esta lista")
print("la palabra Marco está repetida",compuesta.count("Marco"),"veces en esta lista")

## cosas
print(estudiantes[0])  #imprime el dato que está en la posición 1 de la lista, contando desde 0 a la izquierda
print(estudiantes[2]) 
print(estudiantes[-3]) #imprime el dato que está en la posición 3 de la lista, contando desde 1 a la derecha

print(list("Python"))
print(list(range(10)))
print("\n")
