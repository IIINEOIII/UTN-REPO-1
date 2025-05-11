#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#si siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.


#EDAD-CATEGORIA

#SOLICITAMOS UN NUMERO PARA NUESTRA VARIABLE
edad = int(input("Ingrese su edad por favor: "))

#CREAMOS NUESTRA CONDICION
#"SI" LA EDAD ES MENOR A 12
if edad < 12:
#IMPRIMIMOS MENSAJE DE CATEGORIA Niño/a: menor de 12 años.
    print("Niño/ña")

#UTILIZAMOS ELIF "SINO-SI" PARA MULTIPLES CONDICIONES
elif edad >= 12 and edad < 18:
#IMPRIMIMOS MENSAJE DE CATEGORIA Adolescente: mayor o igual que 12 años y menor que 18 años.
    print("Adolescente")

#UTILIZAMOS ELIF "SINO-SI"
elif edad >= 18 and edad < 30:
#IMPRIMIMOS MENSAJE DE CATEGORIA Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    print("Adulto/a joven")

#UTILIZAMOS ELSE "SINO"
else:
#IMPRIMIMOS MENSAJE DE CATEGORIA Adulto/a: mayor o igual que 30 años.
    print("Adulto/a")

