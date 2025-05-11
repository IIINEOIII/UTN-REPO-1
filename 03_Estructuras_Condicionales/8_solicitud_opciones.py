#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.


#Ingresamos un nombre a nuestra variable "nombre"
nombre = input("Ingrese su nombre por favor: ")

#Definimos nuestra variable "numero" en el cual ingresamos un menu que para que nos quede en formato de lista
#utilizamos "\n" para hacer un salto de linea
numero = int(input(
    "Ingrese un numero:\n" 
    "1. Si quiere su nombre en mayúsculas\n"
    "2. Si quiere su nombre en minúsculas\n"
    "3. Si quiere su nombre con la primera letra mayúscula\n"
    "Opcion:" 
))
#Iniciamos nuestra ciondicion "if" que si se cumple la variable "numero" == "1" 
#Se cumplira nuestra primera condicion de la lista
if numero == 1: 
#Imprimimos nuestra variable "nombre" con la funcion ".upper"
   #En el cual convierte todos los caracteres del string en MAYUSCULA.
   print(nombre.upper())

#En nuestra condicion elif si "numero" == "2"
elif numero == 2:
    #En la fuincion ".lower()" convierte todos los caracteres en minuscula.
    print(nombre.lower())
#En nuestra condicion elif si "numero" == "3"
elif numero == 3:
    #En la funcion ".title" transforma la primera letra en MAYUSCULA.
    print(nombre.title())

#Caso contrario en la condicion "else" sino se cumple arrojara un mensaje.
else:
    print("valor no valido")

    