td = 12000 * 10
tn = 16000 * 10
td_d = td + (2000 * 10)
tn_d = tn + (3000 * 10)

Trabajador_1 = {
    "Pago del Lunes":tn,
    "Pago del Martes":tn,
    "Pago del Miercoles":tn,
    "Pago del Jueves":td,
    "Pago del Viernes":td,
    "Pago Semanal":(tn * 3) + (td * 2)
}
print(f"Trabajador 1: {Trabajador_1}")
Trabajador_2 = {
    "Pago del Martes":tn,
    "Pago del Miercoles":tn,
    "Pago del Jueves":tn,
    "Pago del Domingo":td_d,
    "Pago Semanal":(tn * 3) + td_d
}
print(f"Trabajador 2: {Trabajador_2}")
Trabajador_3 = {
    "Pago del Miercoles":td,
    "Pago del Jueves":td,
    "Pago del Viernes":td,
    "Pago del Sabado":tn,
    "Pago del Domingo":tn_d,
    "Pago Semanal":(td * 3) + tn + tn_d
}
print(f"Trabajador 3: {Trabajador_3}")