###############################CONDICIONALES###############################
#Ejemplo:
numeroUno = 10
numeroDos = 2

if(numeroUno > numeroDos): #Si numeroUno es mayor a numeroDos 
    print("se cumple la condicion") #Hace esto
else: #Si la condicion no se cumple
    print("no se cumple la condicion")#hace esto

###############################EJERCITACIONES###############################
#####PARA ESTAS EJERCITACIONES ES NECESARIO IR CAMBIANDO LOS VALORES A LAS VARIABLES PARA VER EL COMPORTAMIENTO DE LOS CONDICIONALES#####

#Declarame una variable que sea un booleano y validá si es verdadero que haga un print indicando que se cumplio la condicion 
# y sino se cumple la condicion otro print indicando que no se cumplio

luz = False 
if(luz == True):
    print("si se cumple la condicion")
else:
    print("no cumple la condicion")



#Declarame una variable que sea una string y despues haceme un condicional que pregunte si la variable que declaraste tiene el valor de un string (vale pedir ayuda)
#Si la condición se cumple mostrame en la terminal el valor de variable dentro de un texto
hola = "hello"
if(type(hola) == str):
    print(f"mi variable es un string y dice :{hola}")


###########Ejercitación de elif###########
#Declarar una variable que sea la nota de un examen (int) si la nota es mayor o igual a 9 que me muestre en pantalla "Excelente!"
#Si es mayor o igual a 7 que muestre "Bien, aprobaste!"
#Si es mayor o igual a 5 que muestre "Uf!, te falto poco para aprobar."
#Si no se cumple ninguna de las condiciones que muestre "Lo lamento pero te fue bastante mal..."
nota= 5
if(nota >= 9):
    print("Excelente!")
elif(nota >= 7):
    print("Bien, aprobaste!")
elif(nota >=5):
    print("Uf!, te falto poco para aprobar.")
else:
    print("Lo lamento pero te fue bastante mal...") 





#Entonces... 
#Un condicional, ejemplo:
#if(condicion <= condicionDos):  
#lo que hace es validar (verificar) si un dato o variable cumple con la condicion que le pasemos
#Se puede usar para validar una infinidad de cosas en la programacion
#Lo importante es saber que el if recibe una (o varias) condicion/es y si se cumple ejecuta el bloque de codigo dentro de la condicion
#Si hay un else y la condicion no se cumple, se ejecuta el bloque de codigo que esta dentro del else

#El uso del elif sirve para hacer condiciones anidadas, es decir, ejecutar primero una condicion (if)
#si no se cumple hacemos otra condicion (elif), la siguiente (elif), si no se cumple la siguiente otro (elif), y asi...
    
###########EJERCITACIÓN FINAL DE CONDICIONALES###########
#Declarar una variable con tu edad y con un condicional validar si la variable existe y tambien si el valor es de tipo string (si se cumple la condicion 
# que muestre en la terminal un mensaje indicando que tipo de valor tiene la variable)
#Luego con otra condicion validar si existe y si el tipo de dato es un entero (si se cumple la condicion que muestre en la terminal un mensaje indicando 
# que tipo de valor tiene la variable)
#Si no se cumple ninguna de las otras condiciones mostrar en la terminal por que la variable llego al else
edad = 51
if(edad and type (edad) == str):
    print(f"el tipo de valor de la variable es : {type(edad)}")
elif(edad and type (edad) == int):
    print(f"el tipo de valor de la variable es : {type(edad)}")
else:
    print(" llego al else por que el tipo de dato de la variable no es un int , tampoco str o quizas la variable no tiene un valor ")
    