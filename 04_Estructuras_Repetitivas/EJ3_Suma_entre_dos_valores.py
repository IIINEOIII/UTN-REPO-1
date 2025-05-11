#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.


#SUMATORIA DE TODOS LOS NUMEROS ENTRE DOS NUMEROS

#1 Primero Solicitamos 2 numeros al usuario
num1 = int(input("Ingrese un primer numero: "))
num2 = int(input("Ingrese un segundo numero: "))

##2 Indicamos cual es mayor y cual es menor para luego sumar los numeros enteros entre esos dos valores

inicio = min(num1, num2) #+1  Esto es lo mismo que la operacion de "inicio = inicio +1"
fin = max(num1, num2)    #-1  Esto es lo mismo que la operacion de "fin = fin - 1"

#3 Ya que no podemos sumar el numero inicial y el final para que arranquemos a contar del siguiente
#numero lo que vamos a realizar es a "inicio" le sumo un numero y a "fin" le resto uno
inicio = inicio +1
fin = fin -1

#4 Creamos nuestr avariable "suma" con valor "0" para luego alojarle resultados
suma = 0 

#5 Creamos nuestro bucle "for" ya que conocemos los rangos de inicio y fin
#  Le agregamos a nuestro "range" un "+1" para que nos tome el ultimo numero antes de range "fin"
for i in range(inicio,fin +1):
    #Realizamos nuestra operacion donde sumamos los numeros del "iterador" que se encuentran entre el rango de "inicio" y "fin"
    suma = suma + i  
    #Imprimimos un mensaje con nuestros resultados
print(f"La suma entre los numeros internos hallados entre {num1} y {num2} es: {suma}")