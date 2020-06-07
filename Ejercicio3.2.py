#Reescribe el programa del salario usando try y except, de modo que el
#programa sea capaz de gestionar entradas no numericas con elegancia,
#mostrando un mensaje y saliendo del programa.

horas = input("Horas trabajadas: ") #Pedimos horas y el dato ingresado lo
#guardamos en la variable horas
tarifa = input("Tarifa: ") #pedimos la tarifa y el dato ingresado lo
#guardamos en la variable tarifa
try:
    horas = float(horas)
    tarifa = float(tarifa)
#Dejamos que el programa convierta los dato de las variables tarifa y horas a
#tipo flotante y los guardamos en su misma variable, si la conversion es
#exitosa nos saltamos el except, si no hay exito, se ejecuta el except
except:
    print("Error, por favor introduzca un numero")
    quit()
#Si no hubo exito en las conersiones, imprimimos un mensaje de error y
#dejamos de ejecutar el programa
if horas <= 40: #Si la variable horas es menor a 40, entra al if y salta el else
    salario = horas * tarifa #multiplicamos tarifa y horas y el resultado lo
    #guardamos en salario
else: #Si horas es mayor a 40, salta el if y entra al else
    horas = horas - 40 #sacamos las horas restantes y las guardamos en horas
    salario = (40 * tarifa) + (horas * (tarifa * 1.5)) #Multiplicamos las
    #primeras 40 horas por la tarifa normal y las horas extra por 1.5 la tarifa
    #normal

print("Salario:", salario) #imprimimos un mensaje y el dato de la variable
#salario 
