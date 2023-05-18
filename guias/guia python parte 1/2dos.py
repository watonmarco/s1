word1 = input("Ingrese la primera palabra: ")
word2 = input("Ingrese la segunda palabra: ")

count1 = len(word1)
count2 = len(word2)

if count1 > count2:
    print(f"La palabra con más caracteres es {word1}, con un total de {count1}")
elif count1 == count2:
    print(f"Las palabras {word1} y {word2} tienen la misma cantidad de caracteres, {count1}")
else:
    print(f"La palabra con más caracteres es {word2}, con un total de {count2}")