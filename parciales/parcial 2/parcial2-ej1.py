palabra = input("ingrese una palabra para saber si se trata de un palindromo: ")
palabra.lower()
# debí crear una variable que a parte con la palabra en minusculas creo
# m_palabra = palabra.lower()
letras = len(palabra)
coincidencias = 0
for i in range(letras):
    if palabra[i] == palabra[(-i) - 1]:
        coincidencias += 1
    else:
        print("no es un palindromo")
        break
    if coincidencias == letras:
        print("es un palindromo")