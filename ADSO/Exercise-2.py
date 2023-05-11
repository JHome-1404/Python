# ADSO EXERCISE 13/10/2022
# @Jesushome1404

# Practice 1
print("Ingrese su materia favorita", "etica", "matematica", "sistema")
Opcion = input("Materia: ")
Materia = Opcion.lower()
if Materia in ("etica", "matematica", "sistema"):
    print("Materia Correcta es: " + Materia)
else:
    print("No Registrada")

# Practice 2
grado = input("Ingrese su Grado: ")
if grado in ("noveno", "decimo", "once"):
    print("Ingrese su Matricula:")
    matricula = input()
    if matricula in ("credito", "contado", "becado"):
        print("Matricula Registrada")
    else:
        print("No se puede Matricular")
else:
    print("<ERROR> GRADO NO ENCONTRADO")


# TALLER
# TALLER

# # Exercise 1
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
if b == 0:
    print("<ERROR> B NO PUEDE SER 0")
else:
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    print("La Suma de", a, "mas", b, "es", suma)
    print("La Resta de", a, "menos", b, "es", resta)
    print("La Multiplicacion de", a, "y", b, "es", multiplicacion)
    print("La Division de", a, "y", b, "es", division)

# Exercise 2
x = int(input("Ingrese el valor de X: "))
y = int(input("Ingrese el valor de Y: "))
z = int(input("Ingrese el valor de Z: "))
a = 0
b = 0
c = 0

if x <= y:
    a = x**2 + y**2
elif x > y:
    a = x - z**2 * y

if y == z:
    b = x**2 + y**2 + z**2
elif y > z:
    b = round(x + (y/z))

if a == b:
    c = a + b
elif a > b or b != 0:
    c = round(a / b)
elif a < b:
    c = a * b

print("A:", a)
print("B:", b)
print("C:", c)
