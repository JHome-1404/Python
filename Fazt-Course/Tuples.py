# DETALLE TUPLAS
# DETALLE TUPLAS

x = (1, 2, 3, 0)
print(x)
print(type(x))

# TUPLAS IN TUPLAS
y = tuple((1, 2, 3))
print(y)

# TUPLAS + RANGE
r = tuple(range(1, 10+1))
print(r)

# print(dir(x))

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',

# 'count', 'index']

# TUPLAS DE UN SOLO ELEMENTO
s = (1)
s = (1,)

m = (1, 2, 3, 4, 5, 0)
print(m[4])

# NO SE PUEDE (ERROR)
# m[4] = 10
# TypeError: 'tuple' object does not support item assignment

# ELIMINAR (ERROR)
del m
print(m)
# NameError: name 'm' is not defined

# DICCIONARIOS + TUPLAS
locations = {
    (35, 12312, 39.0000): "Tokyo",
    (35, 12312, 39.0000): "New York"
}
