N, Q = map(int, input().split())
S = input()
SP = [0]
sb = S[0]
for s in S[1:]:
    if sb == s:
        SP.append(SP[-1]+1)
    else:
        SP.append(SP[-1])
    sb = s
for _ in range(Q):
    l, r = map(int, input().split())
    print(SP[r-1]-SP[l-1])
