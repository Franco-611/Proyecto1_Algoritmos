def shortest_common_supersequence(s1, s2):
    # Caso base: si una de las cadenas está vacía, la otra es la supersecuencia más corta
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    
    # Si los últimos caracteres de ambas cadenas son iguales, podemos agregar uno solo de ellos
    if s1[-1] == s2[-1]:
        return shortest_common_supersequence(s1[:-1], s2[:-1]) + s1[-1]
    
    # De lo contrario, debemos agregar el último carácter de cada cadena y encontrar la supersecuencia más corta entre las dos opciones
    s1_left = shortest_common_supersequence(s1[:-1], s2) + s1[-1]
    s2_left = shortest_common_supersequence(s1, s2[:-1]) + s2[-1]
    if len(s1_left) < len(s2_left):
        return s1_left
    else:
        return s2_left
