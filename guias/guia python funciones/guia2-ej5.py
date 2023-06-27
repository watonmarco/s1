lista = []
x = 0
lista_impares = []
lista_pares = []


while not x==1:
   numeros = int(input("Ingrese su numero en cuestion. Si escribe -1, el programa llegara a su fin: "))
   if numeros== -1:
        break
   
   elif numeros <0:
        print("\n" "este numero no sera agregado a la lista final, porfavor ingrese solo positivos" "\n") 
       
   else:
         lista.append(numeros)


for elementos in lista:
    if elementos % 2 == 0:
        lista_pares.append(elementos)
    else:
        lista_impares.append(elementos)


def escribir_lista_sumada(numeros_sumados):
    numeros_sumados = " + ".join(str(elementos1) for elementos1 in lista)
    print("la sumatoria total seria: ", numeros_sumados ,"=", sum(lista) ) 

escribir_lista_sumada(lista)


def escribir_lista_sumada_impares(lista_impares):
    numeros_sumados_impares = " + ".join(str(elementos2) for elementos2 in lista_impares)
    print("La sumatoria total de los impares sería:", numeros_sumados_impares, "=", sum(lista_impares))

escribir_lista_sumada_impares(lista_impares)


def escribir_lista_sumada_pares(lista_pares):
    numeros_sumados_pares = " + ".join(str(elementos3) for elementos3 in lista_pares)
    print("La sumatoria total de los pares sería:", numeros_sumados_pares, "=", sum(lista_pares))

escribir_lista_sumada_pares(lista_pares)


promedio = sum(lista) / len(lista)
print("el promedio es: ", promedio)


Numero_Mayor = max(lista)
print("el numero mayor ingresado es: ", Numero_Mayor )


if promedio>Numero_Mayor:
    print("el numero es menor que el promedio, y este es: ", Numero_Mayor)
elif promedio==Numero_Mayor:
    print("el numero es igual que el promedio, y este es: ", Numero_Mayor)
else:
    print("el numero es mayor que el promedio, y este es: ", Numero_Mayor )


