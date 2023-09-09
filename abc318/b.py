N = int(input())

Z = [[0]*100 for _ in range(100)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    for y in range(c, d):
        for x in range(a, b):
            Z[y][x] = 1
r = 0
for z in Z:
    r += sum(z)
print(r)
