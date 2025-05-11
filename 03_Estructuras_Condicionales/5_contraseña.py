#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.

#CONTRASEÑA

#DEFINIMOS NUESTRA VARIABLE Y SOLICITAMOS INGRESADO DE DATO
contraseña = input("Ingrese una contraseña entre 8 a 14 caracteres por favor: ")

#INICIAMOS NUESTRA CONDICIO Y UTILIZAMOS
# LA FUNCION "len()" QUE NOS PERMITE OBTENER LA LONGITUD Y MEDIR LA CANTIDAD DE ELEMENTOS DE UN OBJETO
if 8 <= len(contraseña) <= 14:
#IMPRIMIMOS MENSAJE SI SE CUMPLE LA CONDICION
    print("Has ingresado una contraseña correcta")

#CASO QUE NO SE CUMPLA LA CONDICION
else:

#IMPRIMIMOS MENSAJE SI NO SE CUMPLE 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
