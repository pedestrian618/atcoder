def solve(N, edge):
    MAX_N = 25
    dp = [-float('inf')] * (1 << MAX_N)  # dpテーブルの初期化

    dp[0] = 0

    # すべての部分集合sに対して
    for s in range(1 << N):
        u = []
        for i in range(N):
            if not (s & (1 << i)):
                u.append(i + 1)
        for i in range(len(u)):
            for j in range(i + 1, len(u)):
                if edge[u[i]][u[j]]:
                    t = s | (1 << (u[i] - 1)) | (1 << (u[j] - 1))
                    dp[t] = max(dp[t], dp[s] + edge[u[i]][u[j]])

    return max(dp)


# 入力
N = int(input())
weights = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N-1):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        weights[i][j] = r

# 出力
print(solve(N, weights))
