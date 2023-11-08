#Se declaran dos funciones, una con un print y otra con return, aunque son similares, el return devuelve el valor al programa principal

def saludar():
    print("saludo")

def retornarnumero():
    return 1

#Aqui se llaman ambas funciones
saludar()
retornarnumero() 

#Como la segunda funcion tiene un return, se puede hacer algoritmos en el programa principal con ese valor
if retornarnumero()==1:
    print("devolvió un uno")
else:
    print("No devolvió un uno")
