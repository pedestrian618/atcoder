from math import sqrt


def def_rate(P):

    rate = sum(P[i] * (0.9 ** (len(P)-i-1)) for i in range(len(P))) / \
        sum(0.9 ** (len(P)-j-1) for j in range(len(P))) - (1200 / sqrt(len(P)))
    return rate


def calculate_rate(P):
    rate = def_rate(P)
    max_rate = rate
    max_P = P.copy()

    while len(P) > 1:
        min_effect = float('inf')
        min_index = -1
        for i in range(len(P)):
            new_P = P[:i] + P[i+1:]
            new_rate = def_rate(new_P)
            effect = rate - new_rate
            if effect < min_effect:
                min_effect = effect
                min_index = i

        P = P[:min_index] + P[min_index+1:]
        new_rate = def_rate(P)

        if new_rate <= rate:
            break

        rate = new_rate
        max_rate = rate
        max_P = P.copy()

    return max_rate, max_P


N = int(input())
P = list(map(int, input().split()))
print(calculate_rate(P))
