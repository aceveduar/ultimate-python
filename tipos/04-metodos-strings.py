# capitalize, upper son Métodos. Un Método es una función que se encuenta dentro de un objeto.

animal = "chanCHito feliz"

# Mayusculas
print(animal.upper())
# Minusculas
print(animal.lower())
# El primer caracter lo convierte en mayusculas y el resto en minusculas
print(animal.capitalize())
# Toma laprimer letra de cada plabra y las pasa a mayusculas y el resto en minusculas.
print(animal.title())
# Remueve los espacios al principio y al final.
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())

# Podemos encadenar los metodos
print(animal.strip().capitalize())
# Busca caracteres y deveulove el indice.
print(animal.find("fe"))
# Remplaza texto
print(animal.replace("feliz", "triste"))

# Busca caracteres y develve un boleano.
print("feliz" in animal)
print("feliz" not in animal)
