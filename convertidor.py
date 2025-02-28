RomanosaNaturales = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def romanoAnatural(t):
    total = 0
    valor_anterior = 0
    repeticiones = 1
    max_repeticiones = 3

    for i in range(len(t) - 1, -1, -1):
        valor = RomanosaNaturales[t[i]]

        # si el núm se repite
        if i < len(t) - 1 and valor == RomanosaNaturales[t[i + 1]]:
            repeticiones += 1
            # si se repite más de 3 veces bye
            if repeticiones > max_repeticiones:
                print("Error: Número romano no válido (demasiadas repeticiones).")
                return -1
            # si es 5, 50 0 500 no se repite
            if valor in [5, 50, 500]:
                print("Error: Número romano no válido (no se pueden repetir V, L, D).")
                return -1
        else:
            repeticiones = 1

        if valor < valor_anterior:
            total -= valor
        else:
            total += valor

        valor_anterior = valor

    return total


def naturalAromano(n):
    if n <= 0 or n >= 4000:
        return "Error: Número fuera del rango válido (1-3999)."

    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    resultado = ""
    for valor, simbolo in valores:
        while n >= valor:
            resultado += simbolo
            n -= valor

    return resultado

print(romanoAnatural("XV")) # 15
print(romanoAnatural("IX")) # 9
print(romanoAnatural("MCMXC")) # 1990
print(romanoAnatural("IIII")) # Error
print(romanoAnatural("VV")) # Error

print(naturalAromano(15)) # XV
print(naturalAromano(9)) # IX
print(naturalAromano(1990)) # MCMXC
print(naturalAromano(4000)) # Error
