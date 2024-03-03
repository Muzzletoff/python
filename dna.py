from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction, molecular_weight

# Ask the user for input
dna_sequence = input("Enter a DNA sequence: ")

# Create a Seq object from the input
dna_sequence = Seq(dna_sequence)

# Check if the sequence length is a multiple of three
if len(dna_sequence) % 3 != 0:
    print("Warning: The sequence length is not a multiple of three.")
    print("Trimming the sequence to a multiple of three.")
    dna_sequence = dna_sequence[:-(len(dna_sequence) % 3)]

# Print the sequence
print("DNA Sequence:", dna_sequence)

# Get the reverse complement
reverse_complement = dna_sequence.reverse_complement()
print("Reverse Complement:", reverse_complement)

# Calculate GC content
gc_content = gc_fraction(dna_sequence) * 100
print("GC Content:", gc_content, "%")

# Calculate molecular weight
molecular_weight = molecular_weight(dna_sequence)
print("Molecular Weight:", molecular_weight)

# Transcribe the DNA to RNA
rna_sequence = dna_sequence.transcribe()
print("RNA Sequence:", rna_sequence)

# Translate the DNA to protein
protein_sequence = dna_sequence.translate()
print("Protein Sequence:", protein_sequence)

# Find the codons in the DNA sequence
codons = [str(dna_sequence[i:i + 3]) for i in range(0, len(dna_sequence), 3)]
print("Codons:", codons)
