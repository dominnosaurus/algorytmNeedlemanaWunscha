import argparse
from Bio import SeqIO
from algorytm import needlemanWunsch

def readFasta(file_path):
    sequences = []
    with open(file_path, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences.append(str(record.seq))
    return sequences

def saveToFile(outputFile, score, alignments):
    with open(outputFile, "w") as file:
        file.write(f"Score: {score}\n")
        file.write("Alignments:\n")
        for i, alignment in enumerate(alignments, 1):
            file.write(f"\nAlignment {i}:\n")
            file.write(f"Alignment 1: {alignment[0]}\n")
            file.write(f"Alignment 2: {alignment[1]}\n")

def main():
    parser = argparse.ArgumentParser(description="Needleman-Wunsch Algorithm")
    parser.add_argument("--f", dest="fastaFile", required=True, help="Path to the fasta file containing sequences")
    parser.add_argument("--o", dest="outputFile", default="output.txt", help="Path to the output file")
    parser.add_argument("--match", type=int, default=2, help="Score for a match")
    parser.add_argument("--mismatch", type=int, default=-1, help="Penalty for a mismatch")
    parser.add_argument("--gap", type=int, default=-2, help="Penalty for a gap")

    args = parser.parse_args()

    sequences = readFasta(args.fastaFile)

    if len(sequences) < 2:
        print("Error: Provide at least two sequences in the fasta file.")
        return

    sequence1 = sequences[0]
    sequence2 = sequences[1]

    score, alignments = needlemanWunsch(sequence1, sequence2, match=args.match, mismatch=args.mismatch, gap=args.gap)

    print(f"Score (Match={args.match}, Mismatch={args.mismatch}, Gap={args.gap}):", score)
    print("Alignments:")
    for alignment in alignments:
        print("Alignment 1:", alignment[0])
        print("Alignment 2:", alignment[1])
        print()

    saveToFile(args.outputFile, score, alignments)
    print(f"Results saved to {args.outputFile}")


if __name__ == "__main__":
    main()