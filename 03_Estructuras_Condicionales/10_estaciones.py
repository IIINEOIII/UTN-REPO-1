#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|
#           Periodo del año                 |   Estación en el         |   Estación en el     |
#                                           |  hemisferio norte        |   hemisferio sur     |
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|
# Desde el 21 de diciembre hasta el 20 de   |      Invierno            |      Verano          |
#        marzo (incluidos)                  |                          |                      |
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|
# Desde el 21 de marzo hasta el 20 de junio |     Primavera            |      Otoño           |    
#          (incluidos)                      |                          |                      |                                                                          
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|
# Desde el 21 de junio hasta el 20 de       |     Verano               |      Invierno        |    
#          septiembre (incluidos)           |                          |                      |                                                                          
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|
# Desde el 21 de septiembre hasta el 20 de  |     Otoño                |      Primavera       |    
#          diciembre (incluidos)            |                          |                      |                                                                          
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| 

#1-Enero:31
#2-Febrero:28
#3-Marzo:31
#4-Abril:30
#5-Mayo:31
#6-Junio:30 
#7-Julio:31
#8-Agosto:31
#9-Septiembre:30
#10-Octubre:31
#11-Noviembre:30
#12-Diciembre:31

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.

# Función para determinar en que Hemisferio se encuentra:






#Creamos nuestra variable en el cual usamos primero ".strip().upper()" y luego upper en el cual con estas
#funciones hacemos que 1ro:Elimina espacios al inicio y final 2do:Convierte todo en mayuscula
hemisferio = input("¿En que hemisferio estas? (N/S): ").strip().upper()

#Solicitamos un valor numerico para nuestra variable.
mes = int(input("Ingrese un mes del año del (1-12): "))
#Solicitamos un valor numerico para nuestra variable.
dia = int(input("Ingrese un dia del mes (1-31): "))


#Creamos nuestra condicion "if"

#Entre parentesis (mes == 12) hace referencia segun la tabla el mes en el que comenzamos que es "DICIEMBRE"
#En (dia >= 21) hace referencia que este tiene que ser mayor o igual a el 21 de Diciembre y and si estas dos 
#condiciones se cumplen

#Usamos "or" por si unas de estas condiciones se cumple

#En (mes "in" sirve para indicar que los elementos de esta lista [1, 2]) pertenecen a "mes"

#En (mes == 3 and dia <= 20) este es el ultimo mes de la primera tabla y el ultimo dia   

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    #Creampos nuestra condicion "if" que si hemisferio == "N" introducido imprimimos el sig mensaje
    if hemisferio == "N":
        print("Estas en Invierno")
        #Caso contrario
    else:
        #Imprimimos mensaje "VERANO" que correponde a dato opuesto ingresado hemisferio == "S"
        print("Estas en Verano")

#Repetimos como en la condicion anterior solo que ahora iniciamos en el ultimo mes en el que quedamos
#mes 3 que es MARZO y en nuestro operador "or" pasamos al mes "ABRIL y MAYO"
#Por ultimo mes 6 que es "JUNIO"
if (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Estas de Primavera")
    else:
        print("Estas en Otoño")
#Repetimos al igual que en el caso anterior cambiamos los meses que corresponde
if (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Estamos en Verano")
    else:
        print("Estas en Invierno")
#Rpetimos y cambiamos a los ultimos meses que nos faltan
if (mes == 12 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <=20):
    if hemisferio == "N":
        print("Estas en Otoño")
    else:
        print("Estas en Primavera")
else:#Caso contrario que no se cumpla la condicion imprimimos mensaje 
    print("Ingresa una fecha valida")


        
