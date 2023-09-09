N, M, P = map(int, input().split())
re = 0
a = 0
while True:
    m = M + a*P
    if m <= N:
        re += 1
        a += 1
    else:
        print(re)
        exit()
