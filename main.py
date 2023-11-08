import argparse
from Bio import SeqIO
from algorytm import needlemanWunsch

def readFasta(file_path):
    sequences = []
    with open(file_path, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences.append(str(record.seq))
    return sequences

def main():
    parser = argparse.ArgumentParser(description="Needleman-Wunsch Algorithm")
    parser.add_argument("--f", dest="fastaFile", required=True, help="Path to the fasta file containing sequences")

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
if __name__ == "__main__":
    main()