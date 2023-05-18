Algoritmo dos
	definir alumnos, valor_bus, valor_menos30 Como Entero
	Escribir "cantidad de alumnos que viajaran"
	leer alumnos
	
	Si alumnos < 30 y alumnos > 0 Entonces
		valor_menos30 = 550000
		valor_bus = valor_bus + valor_menos30
		escribir "la renta del autobus tiene un valor de: $",valor_bus
	Fin Si
	Si alumnos >= 30 y alumnos <= 49 Entonces
		valor_30_49 = alumnos * 19500
		valor_bus = valor_bus + valor_30_49
		escribir "la renta del autobus tiene un valor de: $",valor_bus
	Fin Si
	Si alumnos >= 50 y alumnos <= 99 Entonces
		valor_50_99 = alumnos * 17000
		valor_bus = valor_bus + valor_50_99
		descuento50 = valor_bus * 0.95
		escribir "la renta del autobus tiene un valor de: $",valor_bus
		escribir "se aplica un descuento del 5%"
		escribir "el totar a pagar es de: $",descuento50
	Fin Si
	Si alumnos >= 100 Entonces
		valor_100 = alumnos * 15000
		valor_bus = valor_bus + valor_100
		descuento100 = valor_bus * 0.9
		escribir "la renta del autobus tiene un valor de: $",valor_bus
		Escribir "se aplica un descuento del 10%"
		Escribir "el total a pagar es de: $",descuento100
	Fin Si
	Si alumnos <= 0 Entonces
		escribir "por favor, ingrese una cantidad valida"
	Fin Si
FinAlgoritmo
