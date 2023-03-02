#Realizamos una función (def) que llamamos determinar estación y toma como parámetro la variable mes.
#Dicha variable mes la usaremos como input en consola. 
#Por ultimo tenemos los condicionales if y elif para revisar que la primera está de Marzo (Mes 3) a Mayo (Mes 5), el verano está desde Junio (Mes 6) hasta agosto (Mes 8), luego verano desde Septiembre (Mes 9) hasta Noviembre (Mes 11) y finalmente el invierno. 

mes = int(input("Ingrese el mes actual (Enero = 1, Diciembre = 12): "))

def determinar_estacion(mes):
    if mes >= 3 and mes <= 5:
        print(f"la estación en el {mes} es primavera")
    elif mes >= 6 and mes <= 8:
        print(f"la estación en el {mes} es verano")
    elif mes >= 9 and mes <= 11:
        print(f"la estación en el {mes} es otoño")
    elif mes >= 12 and mes <= 2:
        print(f"la estación en el {mes} es invierno")
    else:
        print("Ups, lo siento, no reconozco ese mes")


determinar_estacion(mes)