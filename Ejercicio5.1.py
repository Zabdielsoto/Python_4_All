#Escribe un programa que lea repetidamente numeros hasta que el usuario
#introduzca fin. Una vez se haya introducido fin, muestra por pantalla el total
#la cantidad de numeros y la media de esos numeros. Si el ususario introduce
#cualquier otra cosa que no sea un numero, detecta su fallo usando try y except,
#muestra un mensaje de error y pasa al numero siguiente

suma = 0
contador = 0

while True:
    print("Introduzca un numero")
    numero = input(">")
    if numero == 'fin':
        print("\n")
        break
    try:
        numero = float(numero)
    except:
        print("Valor incorrecto, vuelva a intentar")
        continue
    suma = suma + numero
    contador = contador + 1

if contador == 0:
    print("Se ingreso un total de cero valores")
else:
    promedio = suma / contador
    print("La suma total es:",suma)
    print("El numero de valores es:",contador)
    print("El promedio es: ",promedio)
