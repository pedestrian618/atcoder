#O(N log N)
N = int(input())
L = list(map(int,input().split()))
L.sort()
for i in range(1,N):
    if L[i] - L[i-1] > 1:
        print(L[i-1]+1)
        exit()