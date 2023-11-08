#Aqui se hace el uso de funciones lambda, donde estas como tal no tienen la misma estructura que con def, no tienen nombre y por eso son anonimas y puede recibir cualquier cantidad de parametros

numero_palabras = lambda t: len(t.strip().split())
print(numero_palabras("hola, esto es una prueba con lambda"))

#Otro ejemplo distinto de como usar la funcion lambda
for i in range(2):
    
    for j in range(2):
        print(f"{i} & {j} = {operadorand(i, j)}")

operadorand = lambda x, y: x & y

