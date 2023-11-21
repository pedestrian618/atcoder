N, M = map(int, input().split())
A = list(map(int, input().split()))


def find_winners(N, M, votes):
    L = [0] * (N + 1)
    max_votes = 0

    for v in votes:
        L[v] += 1
        if L[v] > max_votes:
            max_votes = L[v]
            c_w = v
        elif L[v] == max_votes and v < c_w:
            c_w = v
        print(c_w)


find_winners(N, M, A)
