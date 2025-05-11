#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).


#Calcular la media de 100 numeros

#Crear nuestro bucle for
#calcular la media
#imprimir resultados

#Creamos nuestra variable "numeros" donde la la lista de los numeros ingresados se almacenaran
numeros = []
#Importamos la funcion mean
from statistics import mean
#Escribimos un mensaje en pantalla explicando lo que hace el programa
print("Ingrese 100 numeros para saber su media")

#Creamos nuestra variable para almacenar
resultado_mean = 0
#Creamos nuestro bucle "for" ya que sabemos el rango de numeros
for i in range (1,101):
    #Solicitamos el ingreso de datos al usuario
    num = int(input(f"Ingrese un numero{i}: "))
    #En nuestra variable "numero" se creara la lista a guardar, mientras ".append" ira guardando los numeros "num" ingresados en orden 
    numeros.append(num)
#En nuestras variable con valor "0" vamos a almacenar nuestro resultado de aplicar la funcion "mean" a nuestra lista de la variable "numeros"    
resultado_mean = mean(numeros)
#Imprimimos el resultado
print("La cantidad de media es: ", resultado_mean)
