# ADSO EXERCISE 13/10/2022
# @Jesushome1404

print("Ingrese el Ejercicio que Deseas Realizar")
opc = int(input())
if opc == 1:
    # Exercise 1
    print("Ingrese un Numero")
    Numero_1 = int(input())
    for i in range(1, Numero_1+1):
        Suma = round(Numero_1*(Numero_1+1) / 2)
    print("La Suma de todos los numeros desde 0 hasta", Numero_1, "es:", Suma)
    # END
elif opc == 2:
    # Exercise 2
    print("Ingrese el Dividendo")
    Numero_2 = int(input())
    print("Ingrese el Divisor")
    Numero_M = int(input())
    Cociente = round(Numero_2 / Numero_M)
    Resto = Numero_2 % Numero_M
    print("El resto de", Numero_2, "y", Numero_M, "es:", Resto)
    print("El Cociente de", Numero_2, "y", Numero_M, "es:", Cociente)
    # END
elif opc == 3:
    # Exercise 3
    print("Ingrese el Valor a Invertir")
    Valor_I = int(input())
    print("Ingrese el Interes Porcentual Anual")
    Porcentual_A = float(input())
    print("Ingrese el Numero de Años")
    a = int(input())
    Na = a*12
    Df = round((Valor_I*Porcentual_A)*Na)
    print("El capital obtenido es:", Df)
    # END
elif opc == 4:
    # Exercise 4
    print("Ingrese la Cantidad de Peluches")
    Cantidad_P = int(input())
    print("Ingrese la Cantidad de Carritos")
    Cantidad_C = int(input())
    Cantidad_Total = Cantidad_P + Cantidad_C
    Peso_Total = (Cantidad_P*100) + (Cantidad_C*70)
    print("La cantidad de Objetos es:", Cantidad_Total,
          "y el Peso Total es:", Peso_Total)
    # END
elif opc == 5:
    # Exercise 5
    print("Ingrese el Numer")
    # END
elif opc == 6:
    # Exercise 6
    print("Ingrese el Numero de Panes Comprados en la Noche")
    Numero_Pan = int(input())
    Precio_Pan = Numero_Pan * 300
    Descuento = round(Precio_Pan * 0.50)
    print("El Precio Habitual del Pan es: COP$ 300 por Pan")
    print("Has recibido un Descuento del 50% de su Compra")
    print("Su Costo Final es:", "COP$", Descuento)
    # END
else:
    print("// ERROR // OPCION NO VALIDA //")
