N = int(input())
# 2で割り続ける
while N % 2 == 0:
    N //= 2
# 3で割り続ける
while N % 3 == 0:
    N //= 3
if N == 1:
    print("Yes")
else:
    print("No")
