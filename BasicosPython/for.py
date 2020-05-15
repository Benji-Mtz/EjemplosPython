numeros = [1,2,3,4,5,6,7,8,9,10]
diccionario = {'a':1, 'b': 2}
tuplas = ((10,20,30), ['string1', 'string 2', ' '],(True,False,True))

for numero in numeros:
    print(numero)
    
for item in diccionario:
    print(diccionario[item])
    

for valor1, valor2, valor3 in tuplas:
    print(valor1, valor2, valor3)
