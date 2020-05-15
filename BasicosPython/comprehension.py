estructura = [ x for x in range(1, 101)]
print(estructura)

tupla = tuple(x for x in range(0, 101) 
                if x % 2 == 0)
print(tupla)

diccionario = { indice:valor
                for indice, valor in enumerate(tupla) }
print(diccionario)                