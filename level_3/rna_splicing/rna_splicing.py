"""
Michael Pacheco 6.22.2022
Complete DNA to protein transformation
taking into account intron deletion/RNA splicing
"""
introns = []


def dna_to_rna(dna_string):
    dna_string = dna_string.replace('T', 'U')

    return dna_string


def rna_2_protein(rna):
    rnaCodonTable = {
        # RNA codon table
        # U
        'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',    # UxU
        'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',    # UxC
        'UUA': 'L', 'UCA': 'S', 'UAA': '\0', 'UGA': '\0',  # UxA
        'UUG': 'L', 'UCG': 'S', 'UAG': '\0', 'UGG': 'W',   # UxG
        # C
        'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',  # CxU
        'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',  # CxC
        'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',  # CxA
        'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',  # CxG
        # A
        'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',  # AxU
        'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',  # AxC
        'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',  # AxA
        'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',  # AxG
        # G
        'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',  # GxU
        'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',  # GxC
        'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',  # GxA
        'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'   # GxG
    }

    codonList = []
    while rna:
        codonList.append(rna[:3])
        rna = rna[3:]
    aaList = []
    for codon in codonList:
        if rnaCodonTable[codon] == '\0':
            break
        aaList.append(rnaCodonTable[codon])
    result = ""
    return result.join(aaList)


def fetch_data_rna_splc():
    dna_string = ''
    with open("rosalind_splc.txt", "r") as f:
        # get rid of first line
        # get dna string
        fasta = f.readlines()
        i = 1
        while i < len(fasta):
            if not fasta[i].startswith(">"):
                fasta[i] = fasta[i].strip("\n")
                if len(fasta[i]) == 60:
                    dna_string += fasta[i]
                if len(fasta[i]) < 60:
                    dna_string += fasta[i]
                    break

            i += 1

        i = i + 2
        while i < len(fasta):
            fasta[i] = fasta[i].strip("\n")
            introns.append(fasta[i])
            i += 2
        introns.sort()
        return dna_string


def delete_introns(rna_string):
    # delete all instances of
    # all introns from rna string
    # find substring of all introns instances
    # including overlapping instances

    for intron in introns:
        rna_string = rna_string.replace(intron, '')

    return rna_string


# fetch_data
dna_string = fetch_data_rna_splc()

# delete introns
dna_string = delete_introns(dna_string)

# convert dna to rna
rna_string = dna_to_rna(dna_string)

# convert rna to protein
protein_string = rna_2_protein(rna_string)
protein_string.replace(" ", '')
print(protein_string)
