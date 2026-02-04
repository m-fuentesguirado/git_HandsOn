#!/usr/bin/env python3

from argparse import ArgumentParser

def nucleotide_percentages(seq):
    seq = seq.upper()
    counts = {"A": 0, "C": 0, "G": 0, "T": 0, "U": 0}

    for nt in seq:
        if nt in counts:
            counts[nt] += 1

    total = sum(counts.values())

    percentages = {}
    for nt in counts:
        if total > 0:
            percentages[nt] = counts[nt] / total * 100
        else:
            percentages[nt] = 0.0

    return counts, percentages

def main():
    parser = ArgumentParser(description="Compute nucleotide percentages for DNA or RNA sequences")
    parser.add_argument("-s", "--seq", required=True, help="Input DNA/RNA sequence")
    args = parser.parse_args()

    counts, percentages = nucleotide_percentages(args.seq)

    print("Counts:")
    for nt in counts:
        print(f"{nt}: {counts[nt]}")

    print("\nPercentages:")
    for nt in percentages:
        print(f"{nt}: {percentages[nt]:.2f}%")

if __name__ == "__main__":
    main()
