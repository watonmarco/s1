def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1
numero = int(input("Ingrese un numero para calcular su factorial: "))
total = factorial(numero)
print(f"el resultado es: {total}")