N,H,X = map(int,input().split())
L = list(map(int,input().split()))
for i,l in enumerate(L):
    if X-H <= l:
        print(i+1)
        exit()