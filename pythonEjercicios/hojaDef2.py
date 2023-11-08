#Se declara una funcion  con un parametro y un return que trabaja con ese return
def raiz(value):
    return value ** (1/2)

#Se imprime una cadena de texto y al tiempo se llama una funcion con un argumento
print(f'La raiz cuadrada es: {raiz(4)}')

#En esta funcion con parametro se verifica la existencia de un objeto a travez de su argumento al ser llamada
def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True")
    else:
        
         print(f"{obj} is False")

validarsiexiste(1)
