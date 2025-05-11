#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

#Suma de rango "0" a numero ingresado

#Solicitamos un numero al usuario positivo
num = int(input("Ingrese un numero positivo para ser calculado desde el rango (0): "))

#Creamos nuestra condicion "if"  por si escribe el usuario un numero negativo, aunque no haga falta esta condiciones

#La creamos para demostrar que podemos tirar un poco de magia en el teclado y sacarle una sonrrisa a la persona que por casualidad lee esto =)
#Espero que estes teniendo un lindo dia facha!! o Hermosa!!
if num < 0:
    #Escribimos un mensaje solicitando que ingrese un numero positivo
    print("Por favor intrdodusca un numero positivo")
#Creamos nuestra condicion "else" en caso de que la condicion "if" no se cumpla, esta pasara a nuestro ciclo "for"
else:

#Creamos nuestra variable suma para almacenar la suma en nuestro ciclo "for"
    suma = 0
#Creamos nuestro ciclo "for" donde el iterador "i" comenzara desde "0" hasta el rango de la variable "num" el cual le concatenamos el "+1" para 
# informar que tiene que ir un rango mas 
    for i in range(num + 1):
        #Nuestra operacion donde se realiza la suma por cada vuelta del iterador "i"
        suma += i
        #Imprimimos los resultados de vuelta de nuestro iterador "i", mas el resultado de la "suma" por cada vuelta del ciclo
        print(f"La suma de 0 hasta {i} es: {suma}")