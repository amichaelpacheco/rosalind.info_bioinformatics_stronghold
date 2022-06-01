# Michael Pacheco
# create consensus and profile for up to 10 given dna strings of length <= 1kbp
# supposed to be O(n^2) for profile creation
# supposed to be O(n) for consensus creation
# i was trying to work around the nested loop by
# creating the profile as we go, however this didn't necessarily work out
# especially without proper knowledge of python

def create_profile_consensus():

    dna_string = ''
    max_length = 0
    f = open("rosalind_cons.txt", "r")
    A = []
    C = []
    G = []
    T = []

    for line in f:
        if line.startswith(">") and dna_string == '':
            continue
        elif line.startswith(">") and dna_string != '':
            # create profile
            max_length = len(dna_string)
            for i, aa in enumerate(dna_string):

                if len(A) != max_length:
                    A.append(0)
                    C.append(0)
                    G.append(0)
                    T.append(0)

                if aa == 'A':
                    A[i] += 1
                elif aa == 'C':
                    C[i] += 1
                elif aa == 'G':
                    G[i] += 1
                elif aa == 'T':
                    T[i] += 1
                else:
                    print("error, non amino acid base char found in dna string!")

                dna_string = ''

        elif not line.startswith(">"):
            line = line.strip('\n')
            dna_string += line

    for i, aa in enumerate(dna_string):

        if aa == 'A':
            A[i] += 1
        elif aa == 'C':
            C[i] += 1
        elif aa == 'G':
            G[i] += 1
        elif aa == 'T':
            T[i] += 1
        else:
            print("error, non amino acid base char found in dna string!")

        dna_string = ''



    # create consensus
    for i, aa in enumerate(A):
        largest_num = A[i]
        largest = 'A'
        if C[i] > largest_num:
            largest_num = C[i]
            largest = 'C'
        if G[i] > largest_num:
            largest_num = G[i]
            largest = 'G'
        if T[i] > largest_num:
            largest_num = T[i]
            largest = 'T'

        print(largest, end="")
    print("")

    # print dna profile
    print("A: ", end=""), print(*A)
    print("C: ", end=""), print(*C)
    print("G: ", end=""), print(*G)
    print("T: ", end=""), print(*T)


create_profile_consensus()
