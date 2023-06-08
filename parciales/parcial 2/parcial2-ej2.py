for i in range(1,11):
    if i == 10:
        i = 0
    numeros = []
    numeros.append(i)
    if i >= 2 and i < 9 or i == 0:
        numeros.append(i + 1)
        numeros.append(0)
        numeros[-1] = i
    elif i == 9:
        numeros.append(0)
        numeros.append(0)
        numeros[-1] = i
    # #
    if i >= 3 and i < 8 or i == 0:
        numeros.insert(2,(i + 2))
        numeros.insert(-1,(i + 1))
        numeros[-1] = i
    elif i == 8:
        numeros.insert(2,(0))
        numeros.insert(-1,(i + 1))
        numeros[-1] = i
    elif i == 9:
        numeros.insert(2,1)
        numeros.insert(-1,0)
        numeros[-1] = i
    # #
    print(numeros)

# # #  el metodo poderoso 
'''n = 11  

for i in range(n):
    linea = ""
    
    for o in range(n - i):
        linea += " "
    
    for o in range(i + 1):
        linea += str((i + o) % 10)
    
    for o in range(i, 0, -1):
        linea += str((i + o - 1) % 10)
    print(linea)'''