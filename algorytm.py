def needlemanWunsch(seq1, seq2, match=2, mismatch=-1, gap=-2):
    lenSeq1 = len(seq1)
    lenSeq2 = len(seq2)

    # matrix innit
    matrix = [[0] * (lenSeq2 + 1) for _ in range(lenSeq1 + 1)]

    # 1st col
    for i in range(lenSeq1 + 1):
        matrix[i][0] = i * gap
    # 1st row
    for j in range(lenSeq2 + 1):
        matrix[0][j] = j * gap

    # fill matrix alg
    for i in range(1, lenSeq1 + 1):
        for j in range(1, lenSeq2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                diagScore = matrix[i - 1][j - 1] + match
            else:
                diagScore = matrix[i - 1][j - 1] + mismatch

            up_score = matrix[i - 1][j] + gap
            left_score = matrix[i][j - 1] + gap

            matrix[i][j] = max(diagScore, up_score, left_score)

    # Znalezienie wszystkich maksymalnych wyników
    max_score = matrix[lenSeq1][lenSeq2]
    alignments = findAlign(matrix, seq1, seq2, match, mismatch, gap)

    return max_score, alignments

def findAlign(matrix, seq1, seq2, match, mismatch, gap):
    alignments = []

    def backtrack(align_seq1, align_seq2, i, j):
        nonlocal alignments

        #finish align
        if i == 0 and j == 0:
            alignments.append((align_seq1, align_seq2))
            return
        #up to 10 alignments
        if len(alignments) >= 10:
            return

        current_score = matrix[i][j]
        diag_score = matrix[i - 1][j - 1] if i > 0 and j > 0 else float('-inf')
        up_score = matrix[i - 1][j] if i > 0 else float('-inf')
        left_score = matrix[i][j - 1] if j > 0 else float('-inf')

        if current_score == diag_score + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            backtrack(seq1[i - 1] + align_seq1, seq2[j - 1] + align_seq2, i - 1, j - 1)
        if current_score == up_score + gap:
            backtrack(seq1[i - 1] + align_seq1, '-' + align_seq2, i - 1, j)
        if current_score == left_score + gap:
            backtrack('-' + align_seq1, seq2[j - 1] + align_seq2, i, j - 1)



    backtrack('', '', len(seq1), len(seq2))
    return alignments