def shortest_common_supersequence_dp(s1, s2):
    # Inicializar la matriz de memoización
    memo = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    # Calcular la longitud de la subsecuencia común más larga para todas las subcadenas de s1 y s2
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    
    # Construir la supersecuencia más corta utilizando la matriz de memorización
    supersequence = ""
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            supersequence = s1[i-1] + supersequence
            i -= 1
            j -= 1
        elif memo[i-1][j] > memo[i][j-1]:
            supersequence = s1[i-1] + supersequence
            i -= 1
        else:
            supersequence = s2[j-1] + supersequence
            j -= 1
    
    # Agregar cualquier carácter restante de s1 o s2 a la supersecuencia
    while i > 0:
        supersequence = s1[i-1] + supersequence
        i -= 1
    while j > 0:
        supersequence = s2[j-1] + supersequence
        j -= 1
    
    return supersequence





    