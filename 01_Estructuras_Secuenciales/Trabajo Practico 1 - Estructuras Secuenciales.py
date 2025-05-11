# Trabajo Practico 1 - Estructuras Secuenciales - Alumno: Romero Juan

# Ejercicio 1

#Imprimimos un mensaje en pantalla
print("Hola Mundo!")

# Ejercicio 2

#A la variable "nombre" le solicitamos un nombre de salida
nombre = input("¿Cuál es tu nombre? ")
#imprimimos en pantalla
print(f"Hola {nombre}!")

# Ejercicio 3

#solicitamos dato a las variables
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
#Imprimimos en pantalla
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4

# importamos "math" para realizar opereacion matematica
import math
#Definimos variable "radio" y solicitamo dato atraves de mensaje
radio = float(input("Ingresá el radio del círculo: "))
#Formula de A= PI * RADIO **2
area = math.pi * radio**2
#Formula de P = 2 * PI * RADIO
perimetro = 2 * math.pi * radio
#Iprimimos en pantalla "AREA y  PERIMETRO"
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

# Ejercicio 5
#Definimos variable en el cual insertado datos atraves de mensaje
segundos = int(input("Ingresá una cantidad de segundos: "))
#Formula H = S/3600
horas = segundos / 3600
#Imprimimos mensaje
print(f"Equivale a {horas} horas")

# Ejercicio 6
#Definimos variable con dato a ingresar
numero = int(input("Ingresá un número: "))
#imprimimos la tabla 
print(f"Tabla del {numero}:")
#Definimos en rango de nuestro Iterador e imprimimos resultado
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
#Solicitamos dato para nuestra variables
a = int(input("Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))
#Imprimimos resultados
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")

# Ejercicio 8
#Solicitamos dato para nuestras variables
peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
#Formula de "indice de masa corporal" e Imprimimos mensaje de salida
imc = peso / (altura ** 2)
print(f"Tu IMC es {imc}")

# Ejercicio 9
#Solicitamos dato
celsius = float(input("Ingresá la temperatura en Celsius: "))
#Formula de Grados Fahrenheint
fahrenheit = (9 / 5) * celsius + 32
#Imprimimos resultado
print(f"La temperatura en Fahrenheit es {fahrenheit}")

# Ejercicio 10
#Solicitud de dato para nuestras variables
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
#Formula de promedio de "3" numeros
promedio = (n1 + n2 + n3) / 3
#Imprimimos resultado
print(f"El promedio es {promedio}")

