#termina_cocal

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.

# Solicita una frase o palabra al usuario
frase = input("Ingresa una frase o palabra: ")

# Verifica si la última letra es una vocal (mayúscula o minúscula)

#frase[-1]: Accede al último carácter del string
#.lower(): Convierte ese carácter a minúscula
#in "aeiou": Comprueba si el último carácter es una vocal
if frase[-1].lower() in "aeiou":
#OPERADOR DE ASIGNACION CONVINADA:(+=) Esto frase += "!" es igual que frase = frase + "!"
#pero usaremos la forma mas sensilla
    frase = frase + "!"  # Añade un signo de exclamación al final

# Imprime el resultado
#SI NO TERMINA EN VOCAL NO SE CUMPLE EL "if" Y PASA DIRECTAMENTE A IMPRIMIR EL MENSAJE "frase"
print(f"Resultado: {frase}")
