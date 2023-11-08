#Aqui se define una funcion con parametros posicionales, que a la hora de llamar se respetara el orden
def compra(marca,cantidad,valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )
#Aqui en el llamado los argumentos van con el orden del parametro
print(f' lo comprado fue:{compra("AMD",3,2500000)}')

#Aqui se trabajan los parametros nominales, es decir se especifica el parametro con su argumento, como se puede ver en el ejemplo
def compra(marca,cantidad,valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )
#A la hora de la llamada, se ve el parametro junto a su argumento, algo asi como clave y valor
print(f' lo comprado fue:{compra(marca="AMD",cantidad=3,valor=2500000)}')