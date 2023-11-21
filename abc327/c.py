A = []
for _ in range(9):
    a = list(map(int, input().split()))
    if len(list(set(a))) != 9:
        print('No')
        exit()
    A.append(a)

for i in range(9):
    temp = []
    for a in A:
        temp.append(a[i])
    if len(list(set(temp))) != 9:
        print('No')
        exit()

for i in range(3):
    for j in range(3):
        temp = []
        for a in A[3*i:3*i+3]:
            for t in a[3*j:3*j+3]:
                temp.append(t)
        if len(list(set(temp))) != 9:

            print('No')
            exit()
print('Yes')
