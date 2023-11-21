N = int(input())
D = list(map(int, input().split()))
r = 0
for i, d in enumerate(D):
    for di in range(d):
        if len(list(set(str(i+1)+str(di+1)))) == 1:
            r += 1
print(r)
