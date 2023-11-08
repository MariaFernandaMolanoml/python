#Otro ejemplo mas de parametros mutables, donde el primero hace que el segundo tenga un valor nuevo
def listaLimpia(arg, result=None): # Define una funcion con nombre 'listaLimpia' que toma dos argumentos, 'arg' y 'result', los cuales tiene un valor predeterminado de None
    if result is None:
        # Si result es None, se crea una lista vacia y se agrega el valor del argumento 'arg' a la lista
        result = []
        result.append(arg)
        print(result)

listaLimpia("a")
listaLimpia("b") 