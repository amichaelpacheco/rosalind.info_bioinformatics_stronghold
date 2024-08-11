"""
Michael Pacheco
Dynamic programming problem about the population of rabbits
Time Complexity:
"""


def calc_rabbit_pop(n, m):
    if n == 1 or n == 2:
        return 1

    # Initialize a list to store the number of rabbit pairs for each i
    rabbit_populations = []
    rabbit_populations.append(0)  # Month 0
    rabbit_populations.append(1)  # Month 1

    for i in range(1, n + 1):
        if i < m:
            rabbit_populations.append(rabbit_populations[i] + rabbit_populations[i - 1])
        elif i == m:
            rabbit_populations.append(
                rabbit_populations[i] + rabbit_populations[i - 1] - rabbit_populations[i - m + 1])
        else:
            rabbit_populations.append(
                rabbit_populations[i] + rabbit_populations[i - 1] - rabbit_populations[i - m])

    return rabbit_populations[n]


# Example usage:
print(calc_rabbit_pop(90, 19))  # Expected output: 4

