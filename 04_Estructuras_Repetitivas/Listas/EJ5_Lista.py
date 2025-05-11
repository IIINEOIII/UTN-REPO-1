#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.


#Lo que realiza el siguiente programa es:

#1) Nos muestra una variable llamdada "numeros" que contiene una lista con los numeros "8, 15, 3, 22, 7"
numeros = [8, 15, 3, 22, 7]

#2) 
# 
# Con remove "Remueve el elemento seleccionado"
# Con max "Selecciona el numero mas grandeo maximo numero"

#Este fragmento nos indica que a esa lista con la funcion "remove" removera el numero "max" que significa maximo, de nuestra lista de la variable "numero"
#Siendo este que removera el numero maximo o mas grande "22"

numeros.remove(max(numeros))

#Imprimimos el resultado en pantalla en el cual muestra la lista, sin el numero "22"
print(numeros)
