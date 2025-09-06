####################################################♥ PRIMER EXAMEN ♥####################################################



#Declarame dos variables que (con un input) pregunten algo que vos quieras para luego hacer un calculo (tercera variable) con lo que te respondio el usuario en en cada pregunta (resta)
#Mostrarme en la terminal que tipo de variable es ahora el calculo
#Transformar el resultado del calculo de entero a string
#Mostrar el resultado del calculo en la terminal dentro de una frase que vos quieras

#Ojo! la frase tiene que estar dividida en dos print y que uno de los dos tenga 2 parametros separados por _
#Objetivo: En la terminal se tiene que ver normal todo junto en la misma linea
valor_uno = input("dame un numero")
valor_dos = input("cuanto le queres restar ?")
calculo = int(valor_uno) - int(valor_dos)
print(type(calculo))
calculo = str(calculo) 
print(f"el resultado de la resta es :{calculo} ") 
print(f"esta dificil pero se puede", end=" ")
print ("jaja", f"el resultado de la resta es {calculo} ", sep= "_")


# TOTAL DE PUNTOS CON AYUDA: 
#Mi novia perfecta se saco un 10 en este primer examen donde uso todo esto que aprendio:
# print 
# sep  
# end 
# variables 
# Reasignacion de variables
# type 
# int 
# str 
# algún calculo 
# bool (falto)
# input 
# {} 
