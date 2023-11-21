from itertools import combinations


def is_connected(subset, N):
    parent = [i for i in range(N+1)]

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        parent[root_v] = root_u

    for u, v, _ in subset:
        union(u, v)

    root = find(1)
    return all(find(i) == root for i in range(2, N+1))


def resolve(N, edges, K):
    min_cost = float('inf')

    for subset in combinations(edges, N-1):
        if is_connected(subset, N):
            cost = sum(w for _, _, w in subset) % K
            min_cost = min(min_cost, cost)

    return min_cost


N, M, K = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))
min_cost = resolve(N, edges, K)
print(min_cost)
