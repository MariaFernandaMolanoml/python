nombres = ['Maria', 'Miguel', 'Angel'] # Definimos una lista con nombres
edades = ['18', '17', '30'] #Definimos una lista con edades, las edades las ponemos en comillas en modo de cadena
for n, e in zip(nombres, edades): # Uso de la función 'zip' para iterar simultaneamente sobre las listas nombres y edades
# La funcion zip combina los elementos de las listas en pares ordenados
    print('Tú nombre es {0}  y tu edad {1}.'.format(n, e)) # Imprime el mensaje, este incluye el nombre y la edad formateados en el orden correspondiente
