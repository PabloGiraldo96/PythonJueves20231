# Rellenar una lista con un valor de entrada (input) y otro input para llenar sus valores 

tamanoLista = int(input("Ingrese por favor el tamaño de la lista: "))

listaUsuario = []

for i in range (tamanoLista):
	numero = int(input('Ingrese un número para añadir a la lista: '))
	listaUsuario.append(numero)

print ('La lista ingresada es: ', listaUsuario)
