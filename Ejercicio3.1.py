#Reescribe el programa del calculo del salario para darle al empleado 1.5
#veces la tarifa horaria para todas las horas trabajadas que excdan de 40

horas = input("Horas trabajadas: ") #Desplegamos un mensaje y esperamos a que
#el usuario ingrese un dato para guardarlo en la variable horas
tarifa = input("Tarifa: ")#Desplegamos un mensaje y esperamos a que
#el usuario ingrese un dato para guardarlo en la variable tarifa

if int(horas) <= 40: #convertimos horas a entero y si es menor que 40,
#entra al if
    salario = float(horas) * float(tarifa) #Convertimos a tipo flotante horas y
    #y tarifa y las multiplicamos, guardamos el resultado en salario
else: #Si horas convertido a entero es mayor a 40, salta el if y entra al else
    horas = float(horas) - 40 #convertimos horas a flotante, le restamos 40 para
    #calcular las horas extra y lo guardamos en horas
    salario = (40 * float(tarifa)) + (horas * (float(tarifa) * 1.5))
    # multiplicamos las 40 horas por la tarifa estandar y las horas extra las
    #las multiplicamos por la tarifa extra que es 1.5 la estandar, el resultado
    #lo guardamos en salario, tarifa es convertida a tipo flotante

print("Salario:", salario) #imprimimos el mensaje y el dato de salario
