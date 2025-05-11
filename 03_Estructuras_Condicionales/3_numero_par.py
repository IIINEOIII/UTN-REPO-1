#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar. 

#NUMEROS PARES

#SOLICITAMOS UN NUMERO PARA NUESTRA VARIABLE
numero = int(input("Ingrese un numero par por favor: "))

#CREAMOS NUESTRA CONDICION IF CON LA ECUACION 
#SI EL NUMERO ES DIVISIBLE POR 2 Y DA COMO RESTO "0" ES PAR
#SI EL NUMERO ES DIVISIBLE POR 2 Y NO DA RESTO "0" ES IMPAR
if numero % 2 == 0:

#IMPRIMIMOS MENSAJE 
    print("Ha ingresado un numero par")

#CASO CONTRARIO USAMOS ELSE
else:

#IMPRIMIMOS MENSAJE
    print("Por favor, ingrese un numero par")