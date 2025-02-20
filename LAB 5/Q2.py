def max_pieces(cuts):
    half = cuts // 2
    return half * (cuts - half)

cuts = int(input("Enter the number of cuts: "))
print("Max pieces with",cuts,"cuts:", max_pieces(cuts))
