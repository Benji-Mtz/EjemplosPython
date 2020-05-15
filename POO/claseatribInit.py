class Usuario:
    
    def __init__(self, username='', correo='', nombre=''):
        self.username = username
        self.correo = correo
        self.nombre = nombre

    def saluda(self):
        return "Hola, soy el usuario: " + self.nombre
    
    def mostrar_username(self):
        print(self.username)
    
    def mostrar_nombre(self):
        print(self.nombre)

codi = Usuario('User_Codi', 'codi@gmail.com', 'Codi')
facilito = Usuario()

resultado = codi.saluda()
print(resultado)