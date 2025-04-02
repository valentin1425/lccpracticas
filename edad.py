#EJERCICIO 4: en una escuela de conducciòn se precisa escribir un progama en el cual
# dependendiendo de la edad de la persona que conduce debe mostrar en pantalla los siguientes mensajes:
# edad < 16 "todavia no puede conducir"
# edad < 18 "puede obtener el permiso de conducir"
# edad > 18 "puede obtener una licencia de conducir"
# edad >= 71 "requiere una licencia especial"


def edadparaconducir(edad):
	
	resultado= ""
	if (edad < 0): 
		resultado= "la edad no puede ser negativa"
	elif (edad < 16):
		resultado=  "todavia no puede conducir"
	elif (edad < 18):
		resultado = "puede obtener el permiso de conducir"
	elif (edad < 70):
		resultado = "puede obtener una licencia de conducir"
	else:ra
	
		resultado = "requiere una licencia especial"
	
	print(resultado)
					
def main():	
	for i in range(0,10):				
		edad = int(input ("ingrese edad: "))
		edadparaconducir(edad)		
			
main()					

		
