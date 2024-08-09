def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(2, 5, 8, 9, 6, 5, 4, 5, 67, 7, 7, 7)
suma(2, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
suma(2, 5, 5, 6, 7, 8, 9)
suma(2, 5, 3, 3, 3, 3, 3)
