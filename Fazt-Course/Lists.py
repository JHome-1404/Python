# DETALLE LISTAS
# DETALLE LISTAS

demo_list = [1, "hello", 1.34, True, [1, 2, 3]]
colors = ["red", "pink", "blue"]

# TUPLA + LISTA
# Tupla convierte a un solo elemento
numbers_list = list((1, 2, 3, 4))
print(numbers_list)

# Para un numero Antes
r = list(range(1, 10+1))
r = list(range(1, 10+1, 2))
print(r)

# print(dir(colors))

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',

#  'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# DIFERENTES
print(len(demo_list))
# Lista dentro de otra cuenta como uno
print(demo_list[4])

# Green esta en colores?
print("pink" in colors)
print("green" in colors)

# METODOS

print(colors)
colors[1] = "yellow"
print(colors)

# AGREGAR ELEMENTOS A UNA LISTA

# No sirve para esta funcion
# colors.append("violet")
# colors.append(("violet", "green"))

# Funciona
# Agrega como solo un elemento
colors.extend(["violet", "green"])
colors.extend(["black", "grey"])

# Inserta en la posicion 1 brown
colors.insert(1, "brown")
colors.insert(-1, "sky")

# Inserta en la de la longitud (ultimo)
colors.insert(len(colors), "orange")

print(colors)

# Quitar Valores (por posicion)
colors.pop()
colors.pop(0)

# Quitar Valores (por contenido)
colors.remove("yellow")

# Ordenar Alfabeticamente
colors.sort()
# Inversamente
colors.sort(reverse=True)

print(colors)

# Obtener Indice (Posicion)
print(colors.index("violet"))
print(colors.index("grey"))

# Contar Numeros de Repeticiones
print(colors.count("grey"))
