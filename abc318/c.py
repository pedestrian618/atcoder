import heapq
N, D, P = map(int, input().split())
F = list(map(int, input().split()))


F.sort(reverse=True)

n1=0
n2=D
cost=0
while True:
    if n2 > N:
        n2 = N
    s = sum(F[n1:n2])
    if P < s:
        cost += P
    else:
        cost += s

    if n2 == N:
        print(cost)
        exit()
    n1 += D
    n2 += D

