#Escribe un programa que le pida al usuario ua temperatura en grados celsius,
#la convierta a grados Farenheit  imprima por pantalla la temperatura convertida

celsius = input("Temperatura en grados Celsius: ")#desplegamos un mensaje,
#esperamos a que el usuario ingrese un dato y lo guardamos en la variable
#celsius

farenheit = ((float(celsius) * 9) / 5) + 32 #convertimos de string a flotante
#la variable celsius, lo multiplicamos por 9, lo dividimos entre 5 y le sumamos
#32 y el resultado lo guardamos en la variable farenheit

print("Temperatura en grados Farenheit:", farenheit)# desplegamos un mnsaje y el
#dato de la variable farenheit
