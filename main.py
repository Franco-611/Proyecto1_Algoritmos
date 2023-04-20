import DAC
import dinamica


S1 = "ABCBDAB"
S2 = "BDCABA"

# Con divide and conquer
print(DAC.shortest_common_supersequence(S1, S2))

DAC.get_graph()

# Con programacion dinamica
print(dinamica.shortest_common_supersequence_dp(S1, S2))

dinamica.get_graph_dp()

#[["ABCD", "ACDF" ],["ABC", "DEF"],["ATCG", "GACT"],["AABB", "ABAB"],["GTAC", "CTAG"],["ACGT", "GATC"],["AGGTAB", "GXTXAYB"],["GCGAGCTGCG", "CGTGCTAGCG"],["AAAGTCTGAC", "TGACTAAACG"],["AAAGTCTGAC", "TGACTAAACG"]]