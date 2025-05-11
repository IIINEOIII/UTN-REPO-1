#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 

#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
# 
#  

#El bloque "try" intenta ejecutar el código que podría causar un error.
#Si todo sale bien, continúa normalmente.
try:
    #Utilzamos "float" en vez de "input" ya que la magnitud puede ser un numero con decimales.
    magnitud_richter = float(input("Ingrese la magnitud del terremoto: "))

    #Creamos nuestra condicion e imprimimos mensaje
    if magnitud_richter < 3:
        print("Muy level (imperceptible)")
    #Si nuestra condicion "and" se cumple, imprimimos mensaje
    elif magnitud_richter >= 3 and magnitud_richter < 4:
        print("Level (ligeramente perceptible)")

    ##Si nuestra condicion "and" se cumple, imprimimos mensaje
    elif magnitud_richter >= 4 and magnitud_richter < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")

    #Si nuestra condicion "and" se cumple, imprimimos mensaje
    elif magnitud_richter >= 5 and magnitud_richter < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")

    #Si nuestra condicion "and" se cumple, imprimimos mensaje
    elif magnitud_richter >= 6 and magnitud_richter < 7:
        print("Muy Fuerte (puede causar daños significativos)")

    #Si nuestra condicion se cumple, imprimimos mensaje
    elif magnitud_richter >= 7:
        print("Extremo (puede causar graves daños a gran escala)")
    
#El bloque except atrapa un error específico si ocurre dentro del try.
#En este caso, ValueError se activa cuando intentas convertir a número algo que no es numérico,
# como letras o símbolos.

except ValueError:
#Imprimimos un mensaje de "ERROR" si ingresamos un caracter invalido.
    print("Error: Ingrese un número válido. No se permiten letras u otros caracteres.")

