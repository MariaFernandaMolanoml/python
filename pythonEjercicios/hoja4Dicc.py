# Creamos un diccionario llamado 'dicaleatorio' utilizando un diccionario por comprension. La clave 'x' esta elevada al cuadrado para los valores 2, 4 y 6
dicaleatorio={x: x**2 for x in (2, 4, 6)}
print(dicaleatorio) #Imprime el diccionario

#IMPRIMIR NÚMEROS EN REVERSA
print("Números en reversa")
for i in reversed(range(1, 10, 2)): # Utiliza la funcion 'reversed' para iterar en reversa sobre un rango de numeros del 1 al 9 en incrementos de 2.
        print(i) # Imprime los numeros en orden inverso


