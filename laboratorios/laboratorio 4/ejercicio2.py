a = [10,80,15,30,20]
b = [20,45,80,20,10]
c = [20,35,60,90,20]

# A
def valor_comun(a,b,c):  # en la hoja no pusimos parámetro
    comun = set(a).intersection(b,c)    # se nos olvidó transformar lista a set
    return comun
print(valor_comun(a,b,c))

# B
def concatenar(a,b,c):  # en la hoja no pusimos parámetro
    abc = set(a).union(b,c)     # lo unico bueno que tuvimos fue ".union(b"
    return abc
print(concatenar(a,b,c))

# C
def chao_dup(a,b,c):  # en la hoja no pusimos parámetro
    set_abc = set(a+b+c)    # aqui no se por que dimos por hecho que si poniamos "abc" ya haría la suma de las listas
    list_abc = list(set_abc)
    return list_abc
print(chao_dup(a,b,c))

# D
no_dup = chao_dup(a,b,c)    # había que crear una variable con el resulado de la funcion chao_dup()

def orden(a,b,c):  # en la hoja no pusimos parámetro
    no_dup.sort(reverse=True)   # no había que crear una nueva variable
    return no_dup
print(orden(a,b,c))

# E
def cien(a,b,c):  # en la hoja no pusimos parámetro
    no_dup[6] = 100
    return no_dup
print(cien(a,b,c))