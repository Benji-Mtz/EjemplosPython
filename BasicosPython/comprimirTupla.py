tupla = (1,2,3,4,5,6)
lista = [10,20,30,40]

resultado = zip(tupla, lista)
resultado1 = list(resultado)

#print('tuple: {0}'.format(resultado1))
print('list: {0}'.format(resultado1))

lista1 = ['hola', 'estamos', 'en', 'python']
tupla1 = ('python', 'java', 'c++')

nueva_tupla = tuple(lista1)
nueva_lista = list(tupla1)

print('nueva tupla: {0}'.format(nueva_tupla))
print('nueva lista: {0}'.format(nueva_lista))