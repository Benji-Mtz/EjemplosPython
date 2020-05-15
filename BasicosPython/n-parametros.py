def crear_usuario(nombre, apellido, edad=9):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{}{}".format(nombre, apellido),
        'edad': edad
    }

codi = crear_usuario(edad=11,apellido='Vazquez',nombre='Spaik')

print(codi['nombre'], codi['apellido'], codi['edad'])