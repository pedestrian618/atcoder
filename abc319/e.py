from sys import stdin
N, X, Y = map(int, stdin.readline().split())
P = []
T = []

for i in range(N-1):
    p, t = map(int, stdin.readline().split())
    P.append(p)
    T.append(t)

Q = int(stdin.readline())
for i in range(Q):
    q = int(stdin.readline())
    c_time = q+X
    for i in range(N-1):
        w_time = (P[i] - c_time % P[i]) % P[i]
        c_time += w_time + T[i]
    c_time += Y
    print(c_time)
