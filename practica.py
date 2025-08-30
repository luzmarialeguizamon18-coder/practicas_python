##El print es para mostrar un mensaje o dato en la terminal##
print("graciasmiamorpreciosoTL")

#Si queres usar comillas ' en el mensaje tenes que usar primero " 
print("Hola quiero decir hola en comillas simples: 'hola'")

##Mandar multiples (VARIOS) parametros al metodo (funcion) print
print("Hola quiero decir hola en comillas simples: 'hola'", "---------------", "tercer parametro")


#Como se puede ver en el ejemplo anterior la coma , que separa los parametros hace un espacio entre cada uno entonces:
##Se escribe como otro parametro para aparte sep = "" y entre las comillas ponemos lo que queremos reemplazar por el espacio.
print("Hola quiero decir hola en comillas simples: 'hola'", "---------------", "tercer parametro", sep = "♥")

#PARA EJECTAR EL ARCHIVO DESDE LA TERMINAL Y PODER VER EL MENSAJE DEL PRINT EJECUTAR EL COMANDO py practica.py EN EL DIRECTORIO ESTE:
#C:\Users\TOMAS\Desktop\Programacion\Luz\practica> 


##Tarea 1: Mostrame en la terminal, tu nombre el mio y el de cielito separados por _
print("LUZ","TOMAS","CIELITO",sep="_")

##Tarea 2: Mostrame en la terminal un mensaje que vos quieras pero que este entre dos corazones
print("♥te","amo","mucho","♥") 

##Tarea 3: Hacer tres print que en la terminal se vean en el mismo renglon y que cada print tenga 2 parametros separados por /
print("hola","miamorcito",sep="/",end=" ")
print("yo","te amo",sep="/",end=" ")
print("mucho","mucho",sep="/")

print("Hola", "mi amorcito yo: ", sep = "_", end = " ")
print("te amo mucho!")
