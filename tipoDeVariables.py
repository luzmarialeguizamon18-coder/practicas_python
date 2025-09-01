#TIPOS DE VARIABLES  (Aca estas declarando la variable hola y asignandole el valor de un string, en la terminal muestra el valor: hola mi amor  ♥ .
hola= " hola mi amor  ♥ "
print (hola)

#Tarea: Declarar una variable, una que sea un string y hacer dos print, uno que me muestre el tipo de dato de tu variable y otro que me muestre el valor de tu variable
eju = " eju jaha " 
print (type(eju)) 
print(eju)

#Tarea: Declarar una variable que tenga un valor entero y mostrarlo en la terminal y luego a esa misma variable asignarle el valor de un string y mostrarlo en la terminal
si_se_puede = 1 
print (si_se_puede)
si_se_puede = "luz"
print (si_se_puede )

#tarea :declarar dos variables , una con tu nombre, otra con tu edad y mostrar en la terminal un mensaje que incluya tu edad y tu nombre (variables)
nombre  = "luz"
edad = 22 
#Con la f antes del string le indicas al print que vas a imprimir un valor o logica entre { }, en este caso mostraste el valor de 2 variables para formar un mensaje
#Esto devuelve en la terminal: mbaeteko luz, tiene 22
print(f"mbaeteko {nombre}, tiene {edad }")

# tarea : usando la variante anterior llamada edad , decirme en un  print que  edad tenias hace dos años 
#En este ejercicio mostras una logica matetica usando tu variable de edad ya declarada anteriormente, este muestra en la terminal: tenia 20 años hace dos años
print (f"tenia {edad-2} años hace dos años")

#Tarea: Declarar 3 variaables dos que sean de tipo string(texto) y la otra de tipo int (entero) y hacer un solo print mostrando una frase en la terminal que incluya tus 3 variables
yo = "luz"
accion = "ir a comprar"
tomate = 5
print(f"{yo},tengo que {accion},{tomate} tomates en el supermecado")

############Tarea : declarar una variable que sea un numero string , luego convertir el  numero string a int y en otra variable sumarle 5.
############finalmente hacer dos print uno que indique  que tipo de datos es la variables y otro print que muestre el valor del variable 
cinco = "5" 
cinco = int (cinco)
calculo = cinco + 5
print (type(calculo))
print (calculo)


# COMANDOS DE GIT PARA SUBIR EL CODIGO A LA NUBE EN ORDEN

# git status: te muestra los cambios que hay en tu proyecto, si no están en verde es que tenes cosas que agregar
# git add . este comando te agrega todos los cambios pero hasta que no haces el commit siguiente y el push no se sube nada
# git commit -m "" y entre las comillas envias un mensaje que describa los cambios que estas subiendo a gitlab (nube)
# git push origin main (sube los cambios a gitlab con tu mensaje del commit)s