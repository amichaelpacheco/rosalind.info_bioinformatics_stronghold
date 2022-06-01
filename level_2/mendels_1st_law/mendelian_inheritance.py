# Michael Pacheco
# O(1)
#given homozygous dominant, heterzygous, and homozygous recessive populations
# find the probability that an offspring of two organisms
# expresses the dominant allele

def probability_dominant(k, m, n):

    S = k + m + n
    # probability recessive = pop_recess/total * (pop_recess-1/total-1 + pop_hetero/(total-1)*2)
    P_R = (n/S) * ((n-1)/(S-1) + m/((S - 1)*2))
    # .5 * (pop_hetero/total) * (pop_recess/(total-1) + (pop_hetero-1)/(total-1)*2)
    P_H = 0.5 * (m/S) * (n/((S-1)+(m-1) / ((S-1)*2)))

    # return 1-(prob_recess+prob_hetero)
    # 1- prob is the probability of the remaining probabilities
    return (1-(P_R+P_H))

#25 23 22
result = probability_dominant(25, 23, 22)
print(result)
