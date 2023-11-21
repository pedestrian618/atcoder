import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
d = {i+1: [] for i in range(N)}
for _ in range(M):
    a, b, x, y = map(int, input().split())
    d[a].append((b, x, y))
    d[b].append((a, -x, -y))
coords = {i: None for i in range(1, N + 1)}
coords[1] = (0, 0)

# BFSで探索
queue = deque([1])
visited = set()

while queue:
    current = queue.popleft()
    visited.add(current)

    for neighbor, x, y in d[current]:
        if neighbor not in visited:
            if coords[neighbor] is None:
                coords[neighbor] = (coords[current][0] + x,
                                    coords[current][1] + y)
            elif coords[neighbor] != (coords[current][0] + x, coords[current][1] + y):
                print("不可能")
                exit()
            queue.append(neighbor)

for i in range(1, N + 1):
    if coords[i] is None:
        print("undecidable")
    else:
        print(*coords[i])
