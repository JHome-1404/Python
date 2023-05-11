# Si la parcela es mayor a 1.000.000m2 la distribuicion es: 70% pinos, 20% Eucaliptos y 10% Cedros
# Si la parcela es menor o iguala 1.000.000m2 la distribuicion es: 50% Pinos, 30% Eucaliptos y 20% Cedros
# Totalice el numero de arboles de cada especie encontrados en la parcela, teniendo en cuenta que: 10m2 caben 2 pinos, en 15m2 caben 15 eucaliptos y 20m2 caben 8 cedros

def parcela(m_parcela):
    if m_parcela > 1000000:
        pin = (0.7*m_parcela//10)*2
        euc = (0.2*m_parcela//15)*15
        ced = (0.1*m_parcela//20)*8
        print("En", m_parcela, "de parcela, hay", pin, "de Pinos,",
              euc, "de Eucaliptos y", ced, "de Cedros")
    elif m_parcela <= 1000000:
        pin = (0.5*m_parcela//10)*2
        euc = (0.3*m_parcela//15)*15
        ced = (0.2*m_parcela//20)*8
        print("En", m_parcela, "de parcela, hay", pin, "de Pinos,",
              euc, "de Eucaliptos y", ced, "de Cedros")


print("Ingrese la cantidad de m2 de la parcela")
print(parcela(int(input())))
