#Escribe un programa para pedirle al usuario el numero de horas y la tarifa por
#hora para calcular el salario bruto

horas = input("Introduzca las horas: ")# desplegamos un mensaje, esperamos a que
#el usuario ingrese un dato y lo guardamos en la variable horas
tarifa = input("Introduzca la tarifa: ")# desplegamos un mensaje, esperamos a que
#el usuario ingrese un dato y lo guardamos en la variable tarifa

salario = float(horas) * float(tarifa)# convertimos de tipo string a tipo
#flotante los datos de las variables horas y tarifa, multiplicamos los dos datos
#y el resultado lo guardamos en la variable Salario
print("Salario:", salario) #desplegamos un mensaje y el dato de la variable
#salario 
