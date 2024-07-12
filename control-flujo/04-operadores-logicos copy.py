# and, or, not

gas = False
encendido = True
edad = 18

if not gas and (encendido or edad > 17):
    print("Puedes avanzar")
else:
    print("You can´t driver")


# Corto circito

""" Permite que la evaluación de una expresión lógica se detenga tan pronto como se determine el resultado final.
 """

# Ejemplo de corto circuito con 'and'
a = False
b = True
resultado = a and b  # 'b' no se evalúa porque 'a' ya es False
print(resultado)  # Salida: False


# Ejemplo de corto circuito con 'or'
a = True
b = False
resultado = a or b  # 'b' no se evalúa porque 'a' ya es True
print(resultado)  # Salida: True
