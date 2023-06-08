t_min = {9,5,2,7,6,1}
t_max = {12,14,11,10,15,9}

# A
if 9 in t_min and 9 in t_max:
    print("La temperatura 9°C esta en ambos sets")
else:
    print("La temperatura 9°C no esta en ambos sets")

# B
if 6 in t_min:
    print("La temperatura 6°C esta en el set de temperaturas minimas")
elif 6 in t_max:
    print("La temperatura 6°C esta en el set de temperaturas maximas")
else:
    print("La temperatura 6°C no esta en ningun set")
if 17 in t_min:
    print("La temperatura 17°C esta en el set de temperaturas minimas")
elif 17 in t_max:
    print("La temperatura 17°C esta en el set de temperaturas maximas")
else:
    print("La temperatura 17°C no esta en ningun set")

# C
min4 = list(t_min)
max4 = list(t_max)

print(min4)
for i in range(len(min4)):   
    min4[i] = min4[i] ** 4
for i in range(len(max4)):   
    max4[i] = max4[i] ** 4

# D
t_min = set(min4)
t_max = set(max4)

ambos = t_min.union(t_max)
print(ambos)
