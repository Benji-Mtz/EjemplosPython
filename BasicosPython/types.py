def saludo(nombre: str) -> None:
    print('Hola ' + nombre)

def suma(num1: int, num2: int = 100) -> int:
    return num1 + num2

nombre = 'Eduardo'
saludo(nombre)

print(suma(10))