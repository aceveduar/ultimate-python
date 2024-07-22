# Ejemplo de como usar la sentencia if

buscar = 3

for numero in range(5):
    print(numero)

    if numero == buscar:
        print("Encontrado ", buscar)
        break
else:
    print("Número no encontrado")


# Los string son iterables
for char in "Ultimate python":
    print(char)
