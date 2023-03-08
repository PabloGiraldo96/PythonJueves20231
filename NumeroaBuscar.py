Lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(f"La lista es: {Lista}")
numeroaBuscar = int(input("Ingrese un número para buscarlo dentro de la lista"))
seEncontro = False    
    
for i in Lista:
    if i == numeroaBuscar:
        seEncontro = True
        break
if seEncontro:
    print(f"el número {numeroaBuscar} se encontró dentro de la lista")
else :
    print(f"el numero {numeroaBuscar} no se encontró")
