contacto = {
    "Nombre":"Marco",
    "Dirección":"No Me Acuerdo #123",
    "Ciudad":"Osorno",
    "Número Telefónico":"933338378"
}
print(contacto)

redes = {
    "Facebook":"Marco Lemarie",
    "Steam":"pairo",
    "Discord":"pairo#3594"
}

contacto["Redes Sociales"] = redes

print("Facebook: ",redes["Facebook"])
print(contacto)