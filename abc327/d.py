from collections import defaultdict
import sys
sys.setrecursionlimit(100000000)
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def is_possible(N, A, B):
    adj_list = defaultdict(set)
    for a, b in zip(A, B):
        adj_list[a].add(b)
        adj_list[b].add(a)

    color = {}

    def dfs(node, c):
        if node in color:
            return color[node] == c
        color[node] = c
        return all(dfs(neigh, c ^ 1) for neigh in adj_list[node])

    for node in range(1, N + 1):
        if node not in color:
            if not dfs(node, 0):
                return False

    return True


if is_possible(N, A, B):
    print('Yes')
else:
    print('No')
