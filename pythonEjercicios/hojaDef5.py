#Los parametros por defecto son donde directamente se le asigna un argumento o valor, en este ejemplo se ve como valor ya tiene un argumento
def compra(marca,cantidad,valor=2500000):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )
#Aqui en la llamada se omite el argumento para valor, y solo se envian dos, que respetan el orden y posicion de los parametros
print(f' lo comprado fue:{compra("AMD",3)}')
