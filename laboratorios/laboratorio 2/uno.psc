Algoritmo uno
	definir costo, tipo, destino Como Entero
	definir peso Como Real
	
	escribir "1. encomienda"
	escribir "2. documento"
	escribir "eliga el tipo de paquete a enviar: "
	Repetir
		leer tipo
		Segun tipo Hacer
			1:
				escribir "1. norteamerica"
				escribir "2. centroamerica"
				escribir "3. sudamerica"
				escribir "4. europa"
				escribir "5. asia"
				escribir "indique el destino del paquete"
				Repetir
					leer destino
					Segun destino Hacer
						1:
							zona = 40
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 50000 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de encomiendas superiores a 50Kg"
							Fin Si
							
						2:
							zona = 30
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 50000 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de encomiendas superiores a 50Kg"
							Fin Si
						3:
							zona = 20
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 50000 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de encomiendas superiores a 50Kg"
							Fin Si
						4:
							zona = 60
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 50000 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de encomiendas superiores a 50Kg"
							Fin Si
						5:
							zona = 70
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 50000 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de encomiendas superiores a 50Kg"
							Fin Si
						De Otro Modo:
							escribir "por favor, indique un destino de la lista"
					Fin Segun
				Hasta Que destino < 6 y destino > 0
				
			2:
				escribir "1. norteamerica"
				escribir "2. centroamerica"
				escribir "3. sudamerica"
				escribir "4. europa"
				escribir "5. asia"
				escribir "indique el destino del paquete"
				Repetir
					leer destino
					Segun destino Hacer
						1:
							zona = 20
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 1500 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de documentos superiores a 1.5Kg"
							Fin Si
							
						2:
							zona = 15
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 1500 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de documentos superiores a 1.5Kg"
							Fin Si
						3:
							zona = 10
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 1500 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de documentos superiores a 1.5Kg"
							Fin Si
						4:
							zona = 30
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 1500 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de documentos superiores a 1.5Kg"
							Fin Si
						5:
							zona = 35
							escribir "indique el peso (en gramos) del envio"
							Repetir
								leer peso
								si peso < 0 Entonces
									escribir "indique un peso valido"
								FinSi
							Hasta Que peso > 0
							costo = peso * zona
							Si peso <= 1500 Entonces
								escribir "el costo del envio es de: $",costo
							SiNo
								escribir "no podemos hacer envios de documentos superiores a 1.5Kg"
							Fin Si
						De Otro Modo:
							escribir "por favor, indique un destino de la lista"
					Fin Segun
				Hasta Que destino < 6 y destino > 0
				
			De Otro Modo:
				escribir "por favor, eliga una opcion valida"
		Fin Segun
		
	Hasta Que tipo < 3 y tipo > 0
	
FinAlgoritmo
