# ADSO EXERCISE 27/10/2022
# @Jesushome1404

# Exercise 1
# Sea la ecuacion: y = x**3 - 3*x**2 - x -5, calcular el valorde x que oscile entre 5 y -5 y que ademas cada vez sufre un incremento de 0.5. Se debe mostrar los valores de x y de y

x = -5
while x <= 5:
    print("Valor de X:", x)
    y = x**3 - 3*x**2 - x - 5
    print("Valor de Y:", y)
    x = x + 0.5

# Exercise 2
# Se tiene una nomina de 10 emleados con la siguiente informacion CODIGO, NOMBRE, VALOR de la HORA, Numero de las Horas trabajdas y Valor de la retencion. Calcular el Salario Neto de cada empleado, se debe mostrar el CODIGO, NOMBRE Y SALARIO Neto de cada empleado
