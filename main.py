from algorytm import needlemanWunsch

sequence1 = "ATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG"
sequence2 = "ATGCTAGCTAGGTAGTTTAGCTAGCTAGCTAGGGSSTAGCTAGAAAAAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCT"
score, alignments = needlemanWunsch(sequence1, sequence2)

print("Score:", score)
print("Alignments:")
for alignment in alignments:
    print("Alignment 1:", alignment[0])
    print("Alignment 2:", alignment[1])
    print()