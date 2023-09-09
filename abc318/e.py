N = int(input())
A = list(map(int, input().split()))
A_set = set(A)
D = {}
for a in A_set:
    D[a] = []
for i, a in enumerate(A):
    D[a].append(i+1)
r = 0
for d in D.values():
    if len(d) > 1:
        d_set = set()
        a = 1
        b = len(d) - 1
        for i in range(min(d)+1, max(d)):
            if i not in d_set:
                r += a*b
            else:
                a += 1
                b -= 1
print(r)
