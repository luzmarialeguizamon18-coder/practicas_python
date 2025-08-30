#en el print se le puede pasar parametros de cualquier tipo de datos por ejemplo un numero 
#Tarea: hacer en un print mi edad y la tuya separadas por _
print("28",22 , sep="_")
#el print tambien sirve para mostrar que tipo de dato es el parametro que le paso al metodo type , el metodo type devuelve que tipo de datos es 
#Tarea: hacer un print que muestre dos tipos de dato, un int (entero) y pasandole tambien un numero pero que sea string (texto), tiene que devolver int y str
 
####El type sirve para saber que tipo de dato es el parametro que le pasamos
print(type(11.5),type("11"), type(11))
print(type(False), end=", ")
print(type(True))

#print de valor no definido
print(type(None))

##Metodo print (muestra en la terminal), que recibe como parametro el metodo type (devuelve que tipo de dato es)
# y ese metodo type recibe el metodo int que es para convertir el tipo de dato a entero, entonces el print devuelve el valor del tipo de dato que es un entero
print(type(int("100")))


#####PARA HACER COMENTARIOS HUMANOS EN EL CODIGO ES # o el """tres ejemplo""" (esto es tres comillas dobles)
""" hola"""
#Hola

#si le envio como parametro 10.1 o cualquier numero con punto a la funcion type va a devolver un  dato de tipo flotante 
############TIPOS DE DATOS############
#str : es un texto definido por comillas "" o ''
#int : es un numero entero como 100 o cualquier numero
#float : es un numero flotante, son todos los que tienen un punto 20.5 o cualquier numero con punto
#NoneType : es cuando el valor que le estamos pasando al metodo type no tiene un valor o no esta definido 

""""Conversion de Datos (convertir un tipo de datos a otro )"""

#Tarea: Hace un print  que haga un suma cualquiera pero el primer numero de la suma tiene que ser un string y el segundo numero tiene que ser un int 
print(int("2")+22)
# el metodo int sirve para pasarle un parametro y convertir ese parametro a un tipo dato "int " o entero .

#Tarea: Hacer un print que concatene un numero string con un numero entero (pista: hay que converter el el entero a string)
print("4"+ str(3))

#Tarea: Haceme tres print convirtiendo en booleanos numeros que el primero y el segundo devuelva false y el tercero devuelva true, incluir un numero negativo
#  (el metodo bool tranforma los numeros en true o false)
print(bool(0))
print(bool(0))
print(bool(- 9))

#Tarea: Hacer dos print usando el metodo bool pasandole string y que uno devuelva true y otro false
print(bool("false"))
print(bool(""))
#Tarea: Lo anterior salio bien por que si al metodo bool le pasas cualuier string con un valor incluso solo un espacio da true, la unica forma que el metodo bool de false es que se le pase asi ""

#Tarea: Mostrame en la terminal dos veces usando el metodo round y el numero 10 en cada print que uno devuelva 11 y otro 10
print(round(10))
print(round(10.6))
#Lo importante del metodo round (redondea) es que si se le pasa como parametro un float (numero con punto), si es menor a la mitad te redondea para abajo y si es mayor redondea para arriba 10.6 = 11 ///// 10.4 = 10
#Si se manda un numero por la mitad (2.5 3.5 10.5) dependiendo el numero redondea para arriba o para abajo (es raro)