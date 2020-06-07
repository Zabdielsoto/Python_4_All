#Ejercicio 6.1 escribe un loop while que empiece en el ultimo caracter en la
#cadena y que vaya bajando hasta el primer caracter de la cadena, imprimiendo
#cada letra en una linea separada

cadena = input("Ingrese una cadena de caracteres: >")
longuitud = len(cadena)

while longuitud > 0:
    letra = cadena[longuitud - 1]
    print(letra)
    longuitud = longuitud - 1
