#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).


#solicitar 100 numeros
#indicar cuantos son pares
#indicar cuales son impares
#cuantos son negativos
#cuando son positivo


#Clasificador de 100 numeros en negativo, pares y impares, positivo

negativo = 0
positivo = 0
impares = 0
pares = 0

for i in range(100):
    print("Bien venido a nuestro programa donde deberar ingresar 100! numeros")
   
    num = int(input("Ingrese un numero: "))

    if num < 0:
        negativo = negativo + 1
    if num > 0:
        positivo = positivo + 1
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
print("Aqui tienes tus resultados")
print("La cantidad de numeros positivos son: ",positivo)
print("La cantidad de numeros negativos son: ",negativo)
print("La cantidad de numeros pares son: ",pares)
print("La cantidad de numeros impares son: ",impares)

    