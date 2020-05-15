def suma(*args):
    total = 0
    for valor in args:
        total += valor
    return total

resultado = suma(10,20,30,40,50)

def combinacion(requerido, *args, **kwargs):
    print(requerido, args, kwargs)

combinacion("valor requerido", 10,20, val1=True, val2=False)