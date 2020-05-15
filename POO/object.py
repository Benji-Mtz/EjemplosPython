class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        #str puede retornar lo que sea
        return self.nombre

class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        #str puede retornar lo que sea
        return self.nombre

gato = Gato('Bigotes')
gato.edad = 6
pato = Pato('Lucas')

print(gato, ' ', pato)
print(gato.__dict__, pato.__dict__)
