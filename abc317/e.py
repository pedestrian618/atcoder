from collections import deque

grid = []

H, W = map(int,input().split())

for h in range(H):
    grid.append(list(input()))
visitable = [[False] * W for _ in range(H)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
directions = {'>': 0, 'v': 1, '<': 2, '^': 3}

for i in range(H):
    for j in range(W):
        if grid[i][j] in directions:
            d = directions[grid[i][j]]
            x, y = i, j
            while True:
                x += dx[d]
                y += dy[d]
                if x < 0 or x >= H or y < 0 or y >= W or grid[x][y] == "#" or grid[x][y] in directions:
                    break
                visitable[x][y] = True

for i in range(H):
    for j in range(W):
        if visitable[i][j]:grid[i][j]= '#'

def find_shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    
    start, goal = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'G':
                goal = (r, c)


    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # BFS
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, 0)])  
    
    while queue:
        (r, c), distance = queue.popleft()

        if (r, c) == goal:
            return distance

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and (grid[nr][nc] == '.' or grid[nr][nc] == 'G'):
                visited[nr][nc] = True
                queue.append(((nr, nc), distance + 1))
    return -1 

print(find_shortest_path(grid))