# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#    deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#PROGRAMA-SOLICITUD-EDAD-MAYOR

#DEFINIMOS NUESTRA VARIABLE Y HACEMOS UN PRONT
edad = int(input("Ingrese su edad por favor: "))

#CREAMOS NUESTRO CONDICION IF EN DONDE EDAD TIENE QUE SER MAYOR A 18
if edad > 18:
    #IMPRIMIMOS MENSAJE SI SE CUMPLE CONDICION
    print("Es mayor de edad")
    
else:
    #IMPRIMIMOS MENSAJE DE SI NO SE CUMPLE CONDICION
    print("No es mayor de edad")
