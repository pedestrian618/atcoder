N = int(input())
S = input()
d = {s: 1 for s in set(S)}
bs, sq = S[0], 1
for s in S[1:]:
    if s == bs:
        sq += 1
        if d[s] < sq:
            d[s] = sq
    else:
        bs, sq = s, 1
result = 0
for v in d.values():
    result += v
print(result)
