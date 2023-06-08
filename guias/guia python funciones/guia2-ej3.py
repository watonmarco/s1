año = int(input("año: "))

def siono():
    if año % 4 == 0:
        return "es bisiesto"
    else:
        return "no es bisiesto"
    
print(siono())