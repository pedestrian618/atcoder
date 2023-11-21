N, X = map(int, input().split())
S = list(map(int, input().split()))
r = 0
for s in S:
    if s <= X:
        r += s
print(r)
