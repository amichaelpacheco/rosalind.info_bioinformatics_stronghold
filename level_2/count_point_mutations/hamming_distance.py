def find_hamming_distance(s, t):
    count = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1

    return len(s) - count

f = open("rosalind_hamm.txt", "r")
dna1 = f.readline()
dna2 = f.readline()
f.close()

result = find_hamming_distance(dna1, dna2)
print(result)