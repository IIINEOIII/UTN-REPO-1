#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.  



# Programa que suma números hasta que el usuario ingrese un 0

#Creamos nuestra variable "suma" donde se va a ir alojando el resultaod de la suma por vuelta
suma = 0

#Creamos nuestra variable "num" donde le solicitamos al usuario un numero para que esta variable aunque sea una vez
#ingrese en nuesto bucle "do-wgile" se compare con la condicion y continue segun lo ingresado
#Si no colocamos in primer imput en nuestra variable, saltara un error ya uque en el bucle la variable "num" no estara definida
num = int(input("Ingrese un número (0 para terminar): "))

#Creamos nuesrtro bulce "while" donde si el "num" es igual a "0" finalizara el programa arrojando de resultado "0"
while num != 0:
    #Creamos nuestra operacion matematica donde alojaremos la suma de los numeros en nuesta variable "suma"
    suma = suma + num
    #Creamos un nuevo imput para solicitar un nuevo numero al usuario, este imput estara dentro del del bucle ya que si no 
    #Se encontrara dentro del bucle, no se repetira el ciclo de solicitar un numero al  usuario
    num = int(input("Ingrese un número (0 para terminar): "))
    
#Imprimimos el resultado en un mensaje
print("El resultado total es:", suma)



    
