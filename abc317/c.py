N, M = map(int,input().split())
graph = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(n):
    if visit[n]:return 0
    visit[n] = True
    d=0
    for q,c in graph[n]:
        if visit[q]:continue
        else: d=max(d,dfs(q)+c)
    visit[n] = False
    return d
ans = 0
for n in range(1,N+1):
    visit = [False]*(N+1)
    ans = max(ans,dfs(n))

print(ans)

