class Animal:
    def comer(self):
        print('Comiendo')
    
    def dormir(self):
        print('Durmiendo')

class Perro(Animal):
    def __init__(self, nombre):
        self.nombre = nombre
    def ladrar(self):
        print('Ladrando')

class Gato(Animal):
    def ronroneo(self):
        print('ronroneo')

ferry = Perro('Ferry')
ferry.ladrar()
ferry.comer()
ferry.dormir()

cat = Gato()
cat.comer()
cat.dormir()