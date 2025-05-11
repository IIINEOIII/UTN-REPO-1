#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.





#CANTIDAD DE DIJITOS



#Solicitar un numero "ENTERO" al usuario
num = int(input("Ingrese un numero entero: "))

#Creamos nuestra variable "origuinal_num" para cuando hagamos un sprit mostremos el numero origuinal del usuario
origuinal_num = num

#Indicamos a nuestro "contador" que es igual a "0"
cont = 0

#Creamos nuestras "3" condiciones donde dependiendo 
#el caso vamos a realizar las siguientes operaciones

#CONDICION 1-
#En esta condicion "if" si el numero ingresado es menor a cero
#Se realiza la siguente Operacion
if num < 0:
    num = -num #Si (num = -22) al ser "-num" esto es igual que hacer esto (-(-22)) convirtiendolo a positivo y alojandolo en "num"

#CONDICION 2-
#En caso de que "num" sea igual a "0" el contador "cont" va a ser igual a "1"
if num == 0:
    cont = 1

#CONDICION 3-
#Si no pasa por ninguna de las anterior condiciones creamos nuestra opcion "else" en el que entra en nuestro bucle "while"
else:
    #Mientras "num" es MAYOR a "0" realizamos nuestra operacion
    while num > 0:
        ##Lo que hacemos aca es que a la variable "num" la dividimos con nuestro operador "//" que lo que hace es sacar la parte entera
        #Es decir al dividir ejemplo 345 // 10 nos dara su parte entera por vuelta 345 // 10 = 34.5 = 34 1ra Vuelta
        num = num // 10                                                           # 34 // 10 = 3.4  = 3  2da Vuelta
                                                                                  #  3 // 10 = 0    = 0  3ra Vuelta

        cont += 1 #Actualizamos nuestra contador                                                                  
        
print(f"La cantidad de caracteres de su numero {origuinal_num} es: {cont}")





    




      