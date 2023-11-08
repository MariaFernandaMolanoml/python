#Aqui se utilizan parametros mutables, es decir que cambian, en donde por medio de un parametro obligatorio, se actualiza el segundo parametro
def lista(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

#Ejercicio: Tomé el presente ejercicio,  y pasé a la función la lista con los días de la semana restantes

diasRestantes = ['sábado','viernes','jueves','miércoles','martes','lunes']

for dia in ['domingo'] + diasRestantes:
    lista(dia)


