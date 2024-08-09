# Ejercicio 2: Par o impar
# Escribe un programa que pida al usuario un número entero y determine si es par o impar.

numero = float(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"Es número {numero} es par")
else:
    print(f"Es número {numero} es Inpar")
