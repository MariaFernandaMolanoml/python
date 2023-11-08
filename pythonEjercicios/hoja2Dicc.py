#Aca se encontrara todo lo que tenga de nombre de variable califiaciones

# Creacion de un diccionario inicial llamado 'calificaciones' con las claves 'nombre' y 'notaFinal' y sus respectivos valores
calificaciones = {
 'nombre': 'Mafe', 
 'notaFinal': 5.0
 }

# Reasignamos la variable calificaciones a un nuevo diccionario con multiples pares de clave-valor
calificaciones = {
 'Mafe': 5.0, 
 'Adriana':5.0,
 'Miguel':4.5,
 'Yessica':2.5
 }

#Uso de un bucle for para iterar sobre los elementos del diccionario 'calificaciones'
for i, j in calificaciones.items():

#Imprime las claves y los valores de cada elemento del diccionario 'calificaciones'
    print(i,j)

# Utilizacion del metodo 'update' para agregar o actualizar elementos dentro del diccionario 'calificaciones'    

calificaciones.update({"Miguel": 5.0, "Paula": 3.8}) 

#BORRAR UN ELEMENTO DEL DICCIONARIO
del(calificaciones['Mafe']) #Elimina la clave 'Mafe' y su valor asociado del diccionario calificaciones
for i, j in calificaciones.items(): # Utiliza un bucle 'for' para iterar sobre los elementos restantes del diccionario calificaciones
    
    print(i,j) # Imprime las claves y los valores de cada elemento restante del diccionario calificaciones

#Estas son las tecnicas para iterar los diccionarios
print("Técnicas por clave") 
for i in calificaciones.keys(): # Utiliza un bucle for para iterar sobre las claves del diccionario 'alificaciones, de este modo imprime cada clave
    print(i)

print("Iterar por valor")
for j in calificaciones.values(): # Utiliza un bucle for para iterar sobre los valores del diccionario calificaciones, de este modo imprime cada valor
    print(j)