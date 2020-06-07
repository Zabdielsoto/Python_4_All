#Escribe un programa que solicite una puntuacion entre 0.0 y 1.0. Si la
#puntuacion esta fuera de ese rango, muestra un mensaje de error. Si la
#puntuacion esta entre 0.0 y 1.0, muestra la calificacion usando la tabla
#siguiente
# >=0.9--Sobresaliente
# >=0.8--Notable
# >=0.7--Bien
# >=0.6--Suficiente
# <0.6--Insuficiente

calificacion = input("Introduzca puntuacion: ") #pedimos la calificacion y el
#dato ingresado lo guardamos en la variable calificacion
try:
    calificacion = float(calificacion)
#Convertimos el dato de la variable calificaion a tipo flotante y lo guardamos
#en esa misma variable, si esto se ejecuta correctamente se salta el except, si
#hay algun error entra al except
except:
    print("Error, introduzca un valor numerico")
    quit()
#Si hay error en el try, entra al except, despliega un mensaje de error y deja
#de ejecutar el programa
if calificacion < 0.6: #si calificacion es menor a 0.6 entra al if|
    print("Insuficiente") #despliega un mensaje
elif calificacion < 0.7: #Si no entro al if anterior y calificacion es menor a
#0.7 entra al if|
    print("Suficiente") #despliega un mensaje
elif calificacion < 0.8:# Si no entro a los if anteriores y calificacion es
#menor a 0.8, entra al if
    print("Bien") #despliega un mensaje
elif calificacion < 0.9: #Si no entro a los if anteriores y calificacion es
#menor a 0.9, entra al if
    print("Notable") #despliega un mensaje
elif calificacion <= 1.0: #si no entro a los if anteriores y calificacion es
#menor o igual a 1.0, entra al if
    print("Sobresaliente") #despliega un mensaje
else: #si no entro a ningun if anterior, entra al else
    print("Puntuacion Incorrecta") #despliega un mensaje 
