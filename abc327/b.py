B = int(input())
R = [a**a for a in range(18)]
if B == 1:
    print(1)
    exit()
for i, r in enumerate(R):
    if B == r:
        print(i)
        exit()
print(-1)
