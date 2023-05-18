# a
Los_Rios = {
    "Nombre":"Los Rios",
    "Superficie":18429,
    "Habitantes":404432
}
Magallanes = {
    "Nombre":"Magallanes",
    "Superficie":1382291,
    "Habitantes":166533
}
diccionario = {
    "ID Region: 14":Los_Rios,
    "ID Region: 12":Magallanes
}
print(diccionario)

# b
dens1 = Los_Rios["Habitantes"] / Los_Rios["Superficie"]
dens2 = Magallanes["Habitantes"] / Magallanes["Superficie"]
Los_Rios["Densidad"] = f"{dens1:.1f}"
Magallanes["Densidad"] = f"{dens2:.1f}"

# c
Los_Rios["Capital"] = "Valdivia"
Magallanes["Capital"] = "Punta Arenas"

# d
com1 = ["Rio Bueno","La Union","Paillaco"]
com2 = ["Cabo de Hornos","Puerto Williams","Porvenir"]
Los_Rios["Comunas"] = com1
Magallanes["Comunas"] = com2

# e
prov1 = ["Ranco","Valdivia"]
prov2 = ["Antartica Chilena","Magallanes","Tierra del Fuego","Ultima Esperanza"]
Los_Rios["Provincia"] = prov1
Magallanes["Provincia"] = prov2

# f
print(diccionario)