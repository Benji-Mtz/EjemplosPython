class Animal:
    def comer(self):
        print('Comiendo')
    
    def dormir(self):
        print('Durmiendo')
    
    def comun(self):
        print('Este es un metodo de Animal')

class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_adopcion = fecha

    def comun(self):
        print('Este es un metodo de Mascota')

class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre
    def ladrar(self):
        print('Ladrando')
    def comun(self):
        print('Este es un metodo de Perro')
    #Sobre-escritura de dormir
    def dormir(self):
        print(self.nombre,"esta durmiendo!")
        #tomando el metodo original del padre
        Animal.dormir(self)
        #agragando mas funciones
        print('No molestar')

class Gato(Animal):
    def ronroneo(self):
        print('ronroneo')

ferry = Perro('Ferry')
ferry.dormir()
# ferry.fecha_adopcion('Hoy')
# ferry.comun()
# print(ferry.fecha_adopcion)