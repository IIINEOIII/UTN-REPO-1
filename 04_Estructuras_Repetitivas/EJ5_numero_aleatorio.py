#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.



#Llamamos nuestra funcion de numero random con "import random"
import random

numero_aleatorio = random.randint(0, 9)

#Creamos nuestra variable en la cual le solicitamos a el usuario que ingrese un numero comprendido ente "0 y 9"

num = int(input("Ingrese un numero entre (0 y 9): "))

#Creamos nuestras variables donde se almacenan el numero de vueltas contadas la cual se le ira sumando "1" y los intentos
inentos = 0
cont = 0

#Creamos nuestro bucle "while" ya que deberemos volver a pedir un numero si no se cumple la condicion


while num != numero_aleatorio: #Nuestra condicion es que si "num" es distinto del "numero_aleatorio" seguira solicitando uno
        
        cont += 1 #A nuestro contador le sumaremos "1" por cada vuelta
        print("Error ese no era!") #Nuestros mensaje si no acierta el numero aleatorio
        print("La cantidad de intentos que llevas son:", cont) #Mostrara la cantidad de intentos con nuestro contador "cont"
        #Solicitamos un nuevo numero para nuestra variable dentro del bucle "while"
        num = int(input("Ingrese un numero entre (0 y 9): "))
 #Mensaje si acierta con el numero aleatorio       
print("Felicitaciones acertaste el numero secreto!")



        
