# DETALLE SRING
# DETALLE SRING

# Comando de Funciones y Metodos que podemos hacer

# print(dir(My_Str))

# FUNCIONES
# FUNCIONES
# Example: print(len(My_Str))

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',

# METODOS
# METODOS
# Example: print(My_Str.find(" "))

# 'capitaliz e', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

My_Str = "Hello World"
My_Str = "hello world car"
My_Str = "hello,world"
My_Str = "hello worldz"

# METODOS
# A los Metodos colocar "()"

# Mayuscula
print(My_Str.upper())
# Minuscula
print(My_Str.lower())
# Cambio de Caracter
print(My_Str.swapcase())
# Primer Mayuscula
print(My_Str.capitalize())

# 2 Metodos
# Reemplazar + Mayuscula
print(My_Str.replace("hello", "bye").upper())
# Contar
print(My_Str.count("l"))

# Empieza con
print(My_Str.startswith("hola"))
print(My_Str.startswith("h"))
# Termina con
print(My_Str.endswith("h"))
print(My_Str.endswith("world"))

# Separa
# Separa apartir de caracter en blanco (Default)
print(My_Str.split())
# .Metodo(Condicion)
print(My_Str.split(","))
print(My_Str.split("o"))

# Encontrar (Posicion)
# Cuando se crea una cadena, cada caracter tiene una posicion(0-h, 1-e, etc..) (Matrices)
print(My_Str.find("o"))
print(My_Str.find(" "))

# FUNCION
# Cuenta Numero de items
print(len(My_Str))

print(My_Str.index("e"))
# Es numerico
print(My_Str.isnumeric())
# Es alphanumerico
print(My_Str.isalpha())

# Posicion (Matrices)
print(My_Str[4])
print(My_Str[0])
# Comienza desde el ultimo
print(My_Str[-1])
print(My_Str[-5])


# CONCATENAR
# CONCATENAR

print("Bitch is " + My_Str)
# Identificador de variable
print(f"Search {My_Str}")
print("Search {0}".format(My_Str))
