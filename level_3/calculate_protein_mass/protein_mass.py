# Michael Pacheco
# O(n) time complexity
# Rosalind: Calculate the protein mass
# of a given amino acid sequence
# where each letter in a
# string of letters has a weight

letters = {"A": 71.03711,
           "C": 103.00919,
           "D":  115.02694,
           "E": 129.04259,
           "F": 147.06841,
           "G": 57.02146,
           "H": 137.05891,
           "I": 113.08406,
           "K": 128.09496,
           "L": 113.08406,
           "M": 131.04049,
           "N": 114.04293,
           "P": 97.05276,
           "Q": 128.05858,
           "R": 156.10111,
           "S": 87.03203,
           "T": 101.04768,
           "V": 99.06841,
           "W": 186.07931,
           "Y": 163.06333}


def calc_protein_mass(s):
    protein_mass = 0
    for amino_acid in s:
        for letter in letters:
            if letter == amino_acid:
                protein_mass += letters[letter]
                break

    return protein_mass

f = open("rosalind_prtm.txt", "r")
string = f.readline()
result = calc_protein_mass(string)
print(result)

