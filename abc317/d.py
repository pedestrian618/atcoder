N = int(input())

tg = 0
total = 0
diff = []
for i in range(N):
    t,a,g = map(int,input().split())
    total += g
    if t>a:tg += g
    else:diff.append((g,((t+a)//(2)) + 1 - t))
if (total//2)+1  <= tg:
    print(0)
    exit()

def find_min_cost(items, g_target):
    max_g = g_target + max(item[0] for item in items)
    costs = [float('inf')] * (max_g + 1)
    costs[0] = 0 
    for g, cost in items:
        for current_g in range(max_g - g, -1, -1):
            if costs[current_g] != float('inf'):
                costs[current_g + g] = min(costs[current_g + g], costs[current_g] + cost)
    return min(costs[g_target:])
print(find_min_cost(diff,(total//2)+1 -tg))