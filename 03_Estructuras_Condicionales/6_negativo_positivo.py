#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
#siguiente: 

#from statistics import mode, median, mean 
#mi_lista = [1,2,5,5,3] 
#mean(mi_lista) 

#En la documentación oficial se puede encontrar más información sobre este paquete: 
#https://docs.python.org/es/3.8/library/statistics.html.  
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 


#● "Sesgo positivo" o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
#mediana es mayor que la moda.
#  
#● "Sesgo negativo" o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#la mediana es menor que la moda. 

#● "Sin sesgo": cuando la media, la mediana y la moda son iguales. 

#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Definir la lista numeros_aleatorios de la siguiente forma:
#  
#import random 
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
#forma aleatoria.


#                             EXPLICACION DE ("MEAN, MEDIAN, MODE")


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#MEAN(media aritmética) Suma todos los valores de una lista y los divide entre la cantidad total de elementos:
#FORMULA MATEMATICA:         x1 + x2...+x3                   5 + 10 + 6
#                   Media = ---------------- = R  Media =  ------------- = 7
#                                 n                              3

#EJEMPLO DE CODIGO:
#import statistics
#datos = [10, 20, 30, 40, 50]
#media = statistics.mean(datos)
#print("Media:", media)   

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#MEDIAN(mediana)Ordena los datos y devuelve el valor del medio:La mediana es el valor que está en el centro cuando los datos están ordenados.
#Si hay una cantidad impar de elementos: la mediana es el del medio ej:
#  [7,1,4] = se ordena [1,4,7] = [4]

#Si hay una cantidad par de elementos: es el promedio de los dos del medio ej:
#  [4, 1, 7, 10] = se ordena [1,4,7,10] = [4,7] = se promedia (4+7)/2 = 5.5

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#MODE(moda): Es el valor que más veces se repite:
#Si hay más de una moda (multimodal),
#puede lanzar un error si no está claro cuál devolver (en versiones anteriores).

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#CODIGO:
#datos = [1, 2, 2, 3, 4]
#moda = statistics.mode(datos)
#print("Moda:", moda)
#Resultado = 2

#Si hay dos valores que se repiten la misma cantidad de veces:

#CODIGO:
#datos = [1, 1, 2, 2]
#moda = statistics.mode(datos)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#IMPORTAMOS CON (from statistics import mode, median, mean)
#LLAMAMOS LA SIGUENTE FUNCION PARA CALCULAR

#"from statistics": Es un módulo de la biblioteca estándar de Python: 
# Para realizar cálculos estadísticos básicos, como promedios, medianas, modas, varianza, desviación estándar, etc.

#"import mode, median, mean": En vez de importar el modulo completo, solo importamos tres funciones (mode,media,mean)
#ES ves de escribir esto e importar todo:    import statistics
#                                            media = statistics.mean(lista)
#                                            from statistics import mode, median, mean

#Importamos directamente y escribimos esto que es mas facil y limpio
#                                            from statistics import mean
#                                            media = mean(lista)
from statistics import mode, median, mean

#IMPORTAMOS "random" PARA GENERAR NUMEROS ALEATORIOS
import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

#media = (mean)
#mediana = (median)
#moda = (mode)
 
 #En nuestra variables llamamos entre parentesis "numeros_aleatorios" creando estos y son procesados 
 #por cada una de nuestras variables "mean, median, mode"
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#Imprimimos nuestros valores arrojados en cada variable
print(f"lista:, {numeros_aleatorios}")
print(f"media: {media}")
print(f"mediana: {mediana}")
print(f"moda: {moda}")

#Creamos nuestra estructura condicional la cual evaluara si el "sesgo es positivo" con la sig formula
if media > mediana > moda:
    print("Sesgo positivo (o a la derecha)")

#Esta estructura condicional evalua si el "sesgo es negativo" con la sig formula
elif media < mediana < moda:
    print("Sesgo negativo (o a la izquierda)")

#Esta estructura condicional evalua "si no hay sesgo"
elif media == mediana == moda:
    print("Sin sego")

#Condicion si no se puede evaluar el "sesgo"
else:
    print("No se puede determinar el Sesgo")





