#Escribe otro programa que pida una lista de numeros como la anterior y al final
#muestre por pantalla el maximo y minimo de los numeros, en vez de la media

maximo = None
minimo = None

contador = 1
print("Ingrese una lista de numeros")

while True:
    contador = str(contador)
    numero = input("Valor " + contador + ": >")

    if numero == 'fin' :
        break

    try:
        numero = float(numero)
    except:
        print("Valor incorrecto, introduzca de nuevo")
        continue

    contador = int(contador)
    if contador == 1:
        maximo = numero
        minimo = numero

    if numero > maximo:
        maximo = numero

    if numero < minimo:
        minimo = numero

    contador = contador + 1

print("El numero mas grande es:", maximo)
print("El numero mas pequeño es:", minimo)
