print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese el primer numero: ")
        if resultado.lower() == "salir":
            break
    resultado = int(resultado)
    op = input("Ingresa operación")

    n2 = ("Ingresa el siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)


if op.lower() == "suma":
    resultado += 2
elif op.lower() == "resta":
    resultado -= 2
elif op.lower() == "multi":
    resultado *= 2
elif op.lower() == "div":
    resultado /= 2
else:
    print("Operacion no valida")
    break

print(f"El resultado es {resultado}")
