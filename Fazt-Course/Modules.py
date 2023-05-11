# MODULOS
# MODULOS

# Modulo o biblioteca

# Es la reutilzacion de codigo para tareas especificas, evitando crear lo ya creado

#  TIPOS DE MODULOS
# Own modules(Mi propio modulo)
# Thirdy party modules(Modulos de Internet o terceros)
# Python modules(Modulos de Python)

# MODULOS PRE-CONSTRUIDOS
# MODULOS PRE-CONSTRUIDOS

# Importa el modulo
from MyMath import add, substract
import MyMath
import datetime
# Importa desde el modulo(datetime) el metodo(timedelta)
from datetime import timedelta, date

# Buscar en google este modulo

# <module> + <class> + <method>
print(datetime.date.today())
# <class> or <method>
# print(date.today())
print(datetime.timedelta(minutes=100))
# print(timedelta(minutes=100))

# MODULOS PROPIOS
# MODULOS PROPIOS
# ir a MyMath.py

# import MyMath
# from MyMath import add, substract

# <module><method>
MyMath.add(1, 2)
# add(1, 2)
MyMath.substract(1, 2)
# substract(1, 2)


# MODULOS DE TERCEROS
# MODULOS DE TERCEROS

# Continuacion en Modules-2.py
