"""
Michael Pacheco
Time complexity: O(n) for a protein of length n,
but the problem states the protein is <= 1000.
"""

# Codon counts for each amino acid
codon_count = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2,
    'I': 3, 'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2,
    'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2,
}

# File name
file_name = 'rosalind_mrna (1).txt'

# Read the file and get the protein string
with open(file_name, 'r') as file:
    protein = file.read().strip()
num_stop_codons = 3

# Compute number of possible RNA strings
num_rna_strings = 1
mod_value = 1000000

for aa in protein:
    num_rna_strings *= codon_count[aa]
    num_rna_strings %= mod_value  # Take module at each step

num_rna_strings *= num_stop_codons
num_rna_strings %= mod_value  # Take modulo after multiplying by stop codons

print(num_rna_strings)