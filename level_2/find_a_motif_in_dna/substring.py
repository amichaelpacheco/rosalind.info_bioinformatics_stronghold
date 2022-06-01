# Michael Pacheco
# given an amino acid sequence find all
# repeating substrings in dna sequence

def find_substring(s, t):
    i = 0
    while i < len(s):
        i = s.find(t, i)
        if i == -1:
            break
        print(i+1)
        i += 1

s = "GTGAGTCTGCACGACTACCGTGCAGGAATACGACTACACGACTAGCACGACTAACGACTAACGACTATTATCTACGACTACTTGCTGGACGACTAGACAGGCTACGACTAGCCTACGACTATACGACTAGACGACTAGACGACTAACGACTAACGACTAACGACTAAGCACGACTAACGACTAACGACTAGATACGACTAGGTGTACGACTAAACGACTAACGACTACGACGACTAAACGACTAAGACGACTATACGACTAACGACTATCCACGACTAATTTGAGAATACGACTACAACGACTAACGACTATTGTAACGACTAGTACGACTAACGACTACTCCACGACTAAACGACTAACGACTAGAACGACTAAACCAACGACTACATGCGACCGCACGACTAGACGACTACCTGCGGACTCGTAACGACTATTGACGACTAGACGACTAGTCAACGACTAACGACTAGGTACGACTACATGTCTCACGACTAACGACTATACGACTAGCGACGACTAGGAACGTGGACGACTACAGACGACTAGGCGACGACTAGTTTACGACTAGATCAAGACCGACGACTAACGACTAACGACTACGGACGACTAGCACGACTAGACGACTAATGCTGACGACTAACGACTACAAACGACTAACGACTAACGACTATTGACGACTAGGAACGACTAGTCACGACTAACGACTACACGACTAGTACGACTAGCGCACGACTACTAACGACTATCTTACGACTAACGACTATGATTCAGGCACAGACGACTAAACGACTAATGGACGACTAGTCA"
t = "ACGACTAAC"

find_substring(s, t)
