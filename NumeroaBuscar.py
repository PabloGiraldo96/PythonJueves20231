#Lista vacía que se llenará con un ciclo for

lista =[]

#Variable booleana que indicará si encontramos el número dentro de la lista (SI / NO)
seEncontro = False

#Ciclo con las 20 vueltas como se pide, y se crea la variable numeros adentro, esta variable es la que va a llenar la lista; con el método .append ingresamos la variable a la lista.
for i in range(0, 20):
    numeros = int(input("Ingrese numero: "))
    lista.append(numeros)

#Ya por fuera del ciclo creamos la variable numeroaBuscar, que se va a comparar con el iterador i y sí cumple la condición entonces la variable seEncontro se vuelve verdadera.
#Luego se imprimen los mensajes si se encontró o no.

numeroaBuscar=int(input("Ingrese numero para ver si está en la lista: "))
for i in lista:
    if i == numeroaBuscar:
        seEncontro = True
        break
if seEncontro:
    print(f"El numero que ingreso {numeroaBuscar} se encuentra dentro de la lista: {lista}")
else:
    print(f"El numero que ingreso {numeroaBuscar} no se encuentra dentro de la lista: {lista}")

