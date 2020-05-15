class Usuario:

    def saluda(self, nombre):
        return "Hola, soy el usuario: " + nombre
    
    def mostrar_username(self):
        print(self.username)
    
    def mostrar_nombre(self):
        print(self.nombre)

    def crear_nombre(self, nombre):
        self.nombre = nombre

codi = Usuario()
codi.username = 'User_Codi'
codi.correo = 'codi@gmail.com'

facilito = Usuario()
facilito.username = 'User_Facilito'
facilito.correo = 'facilito@gmail.com'

codi.crear_nombre('Codi')
codi.mostrar_nombre()