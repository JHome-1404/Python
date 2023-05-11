# BUCLES
# BUCLES

# Tarea tipica con listas de datos
# Recorrer una lista

# FOR
foods = ["apples", "bread", "cheese", "milk", "bananas", "graves"]
# print(foods[0])
# print(foods[1])
# print(foods[2])
# print(foods[3])
# print(foods[4])

# Recorre cada elemento
for food in foods:
    if food == "cheese":
        # print("you have to buy this")
        # break  # Rompe el bucle no sigue imprimiendo
        continue  # Continua con el resto de la ejecucion saltando esta
    print(food)

for number in range(1, 8):
    print(number)

# Recorre cada caracter
for letter in "Hello":
    print(letter)
# H
# E
# L
# L
# O


# WHILE
count = 4
while count <= 10:
    print(count)
    count = count + 1
