# DICCIONARIOS
# DICCIONARIOS

# Sirven para la agrupacion de datos, con ciertos valores, funciones y metodos. Principalmente funcionan para evitar la repeticion de un mismo dato(Codigo largo)

# Carrito de Compras
# Carrito de Compras

# cart = [
#     #Contenido, cantidad, precio, descripcion, descuento
#     ["Book", 3, 4.99, "asassaasas, 0.8"]
#     ["Book", 3, 4.99]
#     ["Book", 3, 4.99]
#     ["Book", 3, 4.99]
# ]

product = {
    "Name": "Book",
    "Quantity": 3,
    "Price": 4.99
}

person = {
    # Keys : Valor
    "First_Name": "Ryan",
    "Last_Name": "Ray"
}

print(type(product))

# print(dir(product))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print(person.keys())
# dict_keys(['First_Name', 'Last_Name'])
print(person.items())
# dict_items([('First_Name', 'Ryan'), ('Last_Name', 'Ray')])

# person.clear()
# print(person)

# RESUMEN
Products = [
    {"name": "book", "price": 10.99},
    {"name": "laptop", "price": 100.99}
]

cart = [
    Products
]

print(Products)
