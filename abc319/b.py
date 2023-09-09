def solve(N):
    s = ['-'] * (N+1)
    for j in range(1, 10):
        if N % j == 0:
            interval = N // j
            for i in range(0, N+1, interval):
                if s[i] == '-' or int(s[i]) > j:
                    s[i] = str(j)

    return ''.join(s)


N = int(input())
print(solve(N))
