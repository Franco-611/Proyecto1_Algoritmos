import DAC
import dinamica


S1 = "ABCBDAB"
S2 = "BDCABA"

# Con divide and conquer
print(DAC.shortest_common_supersequence(S1, S2))

# Con programacion dinamica
print(dinamica.shortest_common_supersequence_dp(S1, S2))