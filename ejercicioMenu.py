import math

opciones = int(input("Ingrese una opción de 1 a 4 : "))

def opcionesDisponibles(opciones):
	if opciones == 0:
		print("Has salido.")
	elif opciones == 1:
		numeroMultiplo = int(input("Ingrese un número para confirmar si es múltiplo de 2: "))
		SiEsMultiplo = numeroMultiplo%2
		if SiEsMultiplo:
			print(f"El número {numeroMultiplo} no es múltiplo de 2")
		else:
			print(f"El número {numeroMultiplo} es múltiplo de 2")
	elif opciones == 2:
		opcionRaiz = int(input("Ingrese un número para buscar su raíz : "))
		numeroRaiz = math.sqrt(opcionRaiz)
		print(f"el número {opcionRaiz} tiene como raíz {numeroRaiz}")
	elif opciones == 3:
		numeroIngresar = int(input("Ingrese un número para sumarle 100 : "))
		numeroIngresado = numeroIngresar + 100
		print(f"el número {numeroIngresar} + 100 da como resultado {numeroIngresado}")
	elif opciones == 4:
		numeroElevarAlCuadrado = int(input("Ingrese un número para elevarlo al cuadrado : "))
		numeroElevado = numeroElevarAlCuadrado * numeroElevarAlCuadrado
		print(f"el cuadrado del número {numeroElevarAlCuadrado} es {numeroElevado}")
	else:
		print("Ups, no encuentro el número que escribes..")

opcionesDisponibles(opciones)