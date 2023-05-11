# IMPORTANTE
# IMPORTANTE

# return sirve para devolver un valor, es decir devuelve a la funcion el valor que le des

# SUMA
# SUMA

# def Suma_Home(num1, num2):
#     return num1 + num2


# print("Ingrese el primer numero")
# numb1 = input()
# print("Ingrese el segundo numero")
# numb2 = input()
# print(Suma_Home(numb1, numb2))

# RESTA
# RESTA

# def Resta_Home(num1, num2):
#     return num1 - num2


# print("Ingrese el primer numero")
# numb1 = input()
# print("Ingrese el segundo numero")
# numb2 = input()
# print(Resta_Home(numb1, numb2))


# def get_even(numbers):
#     even_nums = [num for num in numbers if not num % 2]
#     return even_nums


# print(get_even([1, 2, 3, 4, 5, 6]))


# SALUDAR
# SALUDAR

# def saludo(name="", last_name=""):
#     print("Hello", name, last_name, "What's up?")
#     return input()


# print("Respuesta:", saludo("Jesus", "Home"))

# MULTIPLICAR
# MULTIPLICAR

# def multiplicar(a, b):
#     return a*b


# resultado = multiplicar(10, 5)

# GENERATE PASSWORD
# GENERATE PASSWORD

import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-@"

all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all,length))

print(password)