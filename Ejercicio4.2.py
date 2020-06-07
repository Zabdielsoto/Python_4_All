#Reescribe el programa de calificaciones del capitulo anterior usando una
#funcion llamada calcula_calificaciones, que reciba una puntuacion como
#parametro y devuelva una calificacion como cadena

calificacion = input("Ingrese calificacion: ")#Pedimos un dato para que el
#usuario ingrese la calificacion

try:
    calificacion = float(calificacion)
except:
    print("Puntuacion Incorrecta")
    quit()
#Si la calificaion es un dato numerico y se puede convertir a flotante, se salta
#el else y se sigue con el programa, si la calificacion no es un dato numerico
#entra al else manda un mensaje de error y deja de ejecutar el programa
def calcula_calificacion(calif): #definimos una funcion llamada calcula_calificacion
    if calif <= 0.6: #si la calificacion es menor o igual a 0.6 entra al if
        return("Insuficiente") #retorna un mensaje
    elif calif < 0.7:#si la calificaion es menor a 0.7 y no entro al if anterior
    #entra al if
        return("Suficiente") #retorna un mensaje
    elif calif < 0.8:#si no entro a los if anteriores y la calificaion es menor
    #a 0.8, entra al if
        return("Bien") #retorna un mensaje
    elif calif < 0.9:#Si no entro a los if anteriores y la calificacion es menor
    #a 0.9, entra al if
        return("Notable") #retorna un mensaje
    elif calif <= 1.0:#Si no entro a los if anteriores y la calificacion es menor
    #o igual a 1.0, entra al if
        return("Sobresaliente")#retorna un mensaje
    else:#si no entro a ningun if anterior, entra al else
        return("Puntuacion Incorrecta")#retorna un mensaje

resultado = calcula_calificacion(calificacion) #ejecutamos la funcion usando como
#parametro el dato de la variable calificaion y el dato retornado lo guardamos # -*- coding: utf-8 -*-
#resultado
print(resultado) #imprimimos el dato de resultado
