# Inicialización de las variables
contadora = 1
suma = 0
bandera = True  # Completar aquí, inicializa bandera como True

num1 = int(input("Ingrese un valor N°1:"))

while bandera:
    num2 = int(input("Ingrese un valor N°2:"))
    suma = suma + num2
    contadora = contadora + 1

    while contadora <= num1:  # Completar aquí, la condición debe ser contadora <= num1
        print(suma, end=",")  # Imprimir la suma
        bandera = False

        if contadora >= num1:  # Completar aquí, cambia el operador para que chequeé igual
            bandera = True
            break