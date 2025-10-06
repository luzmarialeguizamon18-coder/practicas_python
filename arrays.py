##################### ARRAYS #####################
#Declara una variable que sea un array de las comidas que te gusten
#Luego mostrame en la terminal (accediendo por el indice del array) las 2 comidas que mas te gustan de todo el array
comidafavorita=["asado", "mandioca", "lomitoArabe", "chessecake"] 
print(f"me gusta comer {comidafavorita[2]} pero tambien el {comidafavorita[0]}")


#Declara una variable que sea un array que contenga 3 arrays:
#Cada uno de esos 3 arrays tiene que tener 2 pociones y en cada posicion de cada array pones lugares que te gustaria ir de vacaciones (sin ningun orden en especifico)
lugares= [["paraguay", "zuiza"],["argentina","mendoza"],["hawai","jamaica"]]


#Luego mostrame un mensaje en la terminal que incluya el lugar que mas te gustaria ir de vacaciones de ese array de arrays

print(f"el lugar que mas quiero ir con mi novio rico delicioso es {lugares[0][1]}")

#Luego mostrame un mensaje en la terminal que muestre el ultimo array de los 3 arrays de tus lugares vacacionales. (Hay que hacer esto de las 2 formas aprendidas)
#(La ultima posicion del array padre (Preguntar)) 
print (lugares[2]) 
print(lugares[-1])