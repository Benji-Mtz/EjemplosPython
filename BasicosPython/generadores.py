def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1,maximo + 1):
        #yield-> return por cada iteración
        yield numero * posicion, numero, posicion
    
for resultado, numero, posicion in tabla_multiplicar(9,20):
    print(numero, "x", posicion, "=", resultado)