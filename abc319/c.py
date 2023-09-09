import time
import itertools
C = []
for _ in range(3):
    c = list(map(int, input().split()))
    for ci in c:
        C.append(ci)
out = []
for i in range(3):
    if len(set(C[i*3:i*3+3])) == 2:
        if C[i*3] == C[i*3+1]:
            out.extend([(i*3, i*3+1, i*3+2), (i*3+1, i*3, i*3+2)])
        elif C[i*3] == C[i*3+2]:
            out.extend([(i*3, i*3+2, i*3+1), (i*3+2, i*3, i*3+1)])
        else:
            out.extend([(i*3+1, i*3+2, i*3), (i*3+2, i*3+1, i*3)])

for i in range(3):
    Ct = [C[i], C[i+3], C[i+6]]
    if len(set(Ct)) == 2:
        if C[i] == C[i+3]:
            out.extend([(i, i+3, i+6), (i+3, i, i+6)])
        elif C[i] == C[i+6]:
            out.extend([(i, i+6, i+3), (i+6, i, i+3)])
        else:
            out.extend([(i+3, i+6, i), (i+6, i+3, i)])

if len(set([C[2], C[4], C[6]])) == 2:
    if C[2] == C[4]:
        out.extend([(2, 4, 6), (4, 2, 6)])
    if C[4] == C[6]:
        out.extend([(6, 4, 2), (4, 6, 2)])
    if C[2] == C[6]:
        out.extend([(6, 2, 4), (2, 6, 4)])

if len(set([C[0], C[4], C[8]])) == 2:
    if C[0] == C[4]:
        out.extend([(0, 4, 8), (4, 0, 8)])
    if C[4] == C[8]:
        out.extend([(8, 4, 0), (4, 8, 0)])
    if C[0] == C[8]:
        out.extend([(8, 0, 4), (0, 8, 4)])


def check_order(seq, order):
    indices = []
    for num in order:
        try:
            idx = seq.index(num)
            indices.append(idx)
        except ValueError:
            return False
    return indices == sorted(indices)


def count_out_combinations(out):
    total_out = 0
    permutations = itertools.permutations(range(9))
    for perm in permutations:
        for o in out:
            if check_order(perm, o):
                total_out += 1
                break
    return total_out


print(1-count_out_combinations(out)/362880)
