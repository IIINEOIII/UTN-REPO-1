#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.



#Solicitaos un numero
num = (input("Ingrese un numero: "))

#Creamos nuestra variable vacia asi guardamos el numero invertido
invertido = ""


#Creamos nuestro bucle "for" para recorrer 
for i in range(len(num) -1, -1, -1):
    invertido += num[i]

#Imprimimos nuestro mensaje en pantalla con el resultado invertido
print("El numero invertido es :", invertido)


