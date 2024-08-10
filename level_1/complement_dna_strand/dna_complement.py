# this function reverses the order of a dna sequence then finds the complement
# for thymine-adenine and guanine-cytosine
def reverse_complement(seq) -> str:
    seq.upper()
    temp = list(seq)
    u = ""
    for i in range(len(temp)):
        if temp[i] == 'T':
            temp[i] = 'A'
        elif temp[i] == 'A':
            temp[i] = 'T'
        elif temp[i] == 'G':
            temp[i] = 'C'
        elif temp[i] == 'C':
            temp[i] = 'G'
        else:
            print("error")

    temp.reverse()
    return u.join(temp)

t = "AAAACCCGGT"
result = reverse_complement(t)
print(result)
