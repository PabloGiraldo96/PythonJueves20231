opcion = 6
listaEmpanadas =[]

print ("**EMPANADAS DON BAZUQUITO***")
print ("1. Registrar empanada")
print ("2. Mostrar empanada")
print ("3. Buscar empanada")
print ("4. Editar empanada")
print ("5. Eliminar empanada")
print ("6. Salir")

# Variable contador (Será igual al id de la empanada y se autoincrementará, llevando el control del empanada["id"])
contador = 1

while opcion != 0:
    opcion = int(input("Ingrese por favor un numero del menú: "))  
    if opcion == 1:
        empanada = {}
        empanada["id"] = contador
        contador +=1
        empanada["nombre"] = input("Digita el nombre de la empanada: ")
        empanada["precio"] = int(input("Digita el precio de la empanada: "))
        empanada["fechaFabricacion"] = input("Digita la fecha de fabricacion: ")
        empanada["popularidad"] = int(input("Digite la popularidad: "))     
        listaEmpanadas.append(empanada)
    elif opcion == 2:
        print(f"Actualmente, esta es la lista de empanadas que tenemos {listaEmpanadas}")
    elif opcion == 3:
        empanadaAbuscar = int(input("Digita el codigo de la empanada: "))
        #Variable booleana que controlará la repetición del mensaje dentro del ciclo
        bandera = False
        for empanadaSeleccionada in listaEmpanadas:
            if empanadaSeleccionada["id"] == empanadaAbuscar:
                print(f"La empanada que busca es: {empanadaSeleccionada}")
                bandera = True
                break
        if not bandera:
                print("No se encontro empanada")
    elif opcion == 4:
        empanadaAbuscar = int(input("Digita el codigo de la empanada: "))
        for empanadaSeleccionada in listaEmpanadas:
            if empanadaSeleccionada["id"] == empanadaAbuscar:
                empanadaSeleccionada["precio"] = float(input("Digite nuevo precio: "))
                bandera = True
                break
            else:
                print("No se encontro empanada")
    elif opcion == 5:
        empanadaAbuscar = int(input("Digita el codigo de la empanada que desea eliminar: "))
        for empanadaSeleccionada in listaEmpanadas:
            if empanadaSeleccionada["id"] == empanadaAbuscar:
                listaEmpanadas.remove(empanadaSeleccionada)
                print(f"La empanada se ha eliminado con éxito, la lista de empanadas ha quedado así {listaEmpanadas}")
                break
    elif opcion == 6:
                print("Gracias por guardar y eliminar empanadas en empanadas don bazuquito, chao")
                break
    else:
        print("No encuentro el número que escribes..")
