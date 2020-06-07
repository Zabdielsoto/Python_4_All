#Reescribe el programa de calculo del salario, con tarifa y media para las horas
#extras, y crea una funcion llamada calculo_salario que reciba dos parametros}
#(horas y tarifa)

horas = input("Introduzca horas trabajadas: ") #Pedimos las horas y esperamos a
#que el usuario ingrese un dato para guardarlo en la variable horas
tarifa = input("Introduzca tarifa: ") #Pedimos la tarifa y esperamos a que el
#usuario ingrese un dato para guardarlo en la variable tarifa

try:
    horas = float(horas)
    tarifa = float(tarifa)
    #Dentro del try intentamos convertir los datos de las variables a tipo
    #foltante, si se hace exitosamente, se salta el except, si no, lo ejecuta
except:
    print("Error, introduzca datos numericos")
    quit()
    #Si el las lineas del try no se ejecutan bien, entra al except, se imprime
    #un mensaje de error y se deja de ejecutar el programa

def calculo_salario(horas,tarifa): #Definimos una funcion llamada calculo_salarial
#que trabaja con dos parametros
    if horas <= 40: #si las horas son menores o igual a 40, entra al if
        salario = horas * tarifa# calculamos el salario multiplicando las horas
        #por la tarifa
    else: #Si las horas son mayores a 40, entra al else
        horas = horas - 40 #Calculamos las horas que extras
        salario = (40 * tarifa) + (horas * (tarifa * 1.5)) #Calculamos el salario
        #multiplicando las 40 horas por la tarifa normal y multiplicando las
        #horas extra por 1.5 la tarifa normal
    return(salario) #Se acaba la funcion y retornamos el dato de la variable salario

salario = calculo_salario(horas,tarifa) #Ejecutamos la funcion usando como parametros
#los datos de la variable horas y tarifa y el valor que retorna la funcion lo
#guardamos en la variable salario
print("Salario:", salario) #Imprimimos un mensaje y el valor de salario 
