"""

"""
# Importa el módulo random, el cual permite generar valores aleatorios
import random

# Ejemplo 1: Generar un número entero aleatorio
print("Uso de random.randint()")

# random.randint(a, b) genera un número entero aleatorio en el rango [a, b]
numero_aleatorio = random.randint(1, 100)  
print(f"Número aleatorio entre 1 y 100: {numero_aleatorio}")  
# Salida esperada: Un número aleatorio entre 1 y 100, por ejemplo: 57

print("---------------------")

# Ejemplo 2: Seleccionar un elemento aleatorio de una lista
print("Uso de random.choice()")

# Se define una lista con diferentes provincias de Ecuador
provincias = ["Loja", "Azuay", "Pichincha", "Guayas", "Esmeraldas"]
# random.choice(lista) selecciona un elemento aleatorio de la lista
provincia = random.choice(provincias)
print(f"Provincia seleccionada: {provincia}")
# Salida esperada: Una provincia aleatoria de la lista, por ejemplo: Loja

print("---------------------")


# Ejemplo 3: Desordenar aleatoriamente los elementos de una lista 
print("Uso de random.shuffle()")

# Se define una lista con números del 1 al 5
numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")
# random.shuffle(lista) desordena los elementos de la lista
random.shuffle(numeros)
print(f"Lista desordenada: {numeros}")
# Salida esperada: La lista con los mismos elementos pero en un orden diferente, 
# por ejemplo: [3, 1, 5, 2, 4]
