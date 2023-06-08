import random

valor = random.randrange(100,15000,10)
print(f"el producto tiene un valor de: ${valor}")

pago = int(input("con cuanto efectivo desea pagar?\n"))


def cajero(valor,pago):
    billetes = [20000,10000,5000,2000,1000]
    monedas = [500,100,50,10]
    vuelto = []

    diferencia = pago - valor

    for i in billetes:
        if diferencia >= i:
            cuenta = diferencia // i
            diferencia -= cuenta * i
            vuelto.append(f"billete de {i}(x{cuenta})")
    for i in monedas:
        if diferencia >= i:
            cuenta = diferencia // i
            diferencia -= cuenta * i
            vuelto.append(f"moneda de {i}(x{cuenta})")
    return vuelto

print(cajero(valor,pago))