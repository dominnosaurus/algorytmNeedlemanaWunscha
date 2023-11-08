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

    args = parser.parse_args()

    sequences = readFasta(args.fastaFile)

    if len(sequences) < 2:
        print("Error: Provide at least two sequences in the fasta file.")
        return

    sequence1 = sequences[0]
    sequence2 = sequences[1]

    score, alignments = needlemanWunsch(sequence1, sequence2)

    print("Score:", score)
    print("Alignments:")
    for alignment in alignments:
        print("Alignment 1:", alignment[0])
        print("Alignment 2:", alignment[1])
        print()

    saveToFile(args.outputFile, score, alignments)
    print(f"Results saved to {args.outputFile}")


if __name__ == "__main__":
    main()