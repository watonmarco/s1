ciudades = ["Santiago","Temuco","Osorno","Punta arenas"]
ica = [134,99,245,50]

icamin = ica.index(min(ica))
print(f"La ciudad con el íncice más bajo es {ciudades[icamin]} con {min(ica)}")

icamax = ica.index(max(ica))
print(f"La ciudad con el íncice más alto es {ciudades[icamax]} con {max(ica)}")

for i in range(len(ciudades)):
    if ica[i] >= 0 and ica[i] <= 50:
        print(f"{ciudades[i]} tiene un índice de calidad de aire Bueno")
    elif ica[i] >= 51 and ica[i] <= 100:
        print(f"{ciudades[i]} tiene un índice de calidad de aire Moderado")
    elif ica[i] >= 101 and ica[i] <= 150:
        print(f"{ciudades[i]} tiene un índice de calidad de aire Dañino para la salud de grupos sensibles")
    elif ica[i] >= 151 and ica[i] <= 200:
        print(f"{ciudades[i]} tiene un índice de calidad de aire Dañino para la salud")
    elif ica[i] >= 201 and ica[i] <= 250:
        print(f"{ciudades[i]} tiene un índice de calidad de aire Muy dañino para la salud")
    else:
        print(f"{ciudades[i]} tiene un índice de calidad de aire Peligroso")