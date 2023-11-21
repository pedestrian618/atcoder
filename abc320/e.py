import sys
import heapq
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
events = [tuple(map(int, input().split())) for _ in range(M)]
amounts = [0] * N
queue = deque(range(1, N+1))
return_queue = []

for event in events:
    T, W, S = event

    while return_queue and return_queue[0][0] <= T:
        _, person = heapq.heappop(return_queue)
        queue.appendleft(person)

    if queue:
        person = queue.popleft()
        amounts[person-1] += W
        heapq.heappush(return_queue, (T+S, person))

for amount in amounts:
    print(amount)
