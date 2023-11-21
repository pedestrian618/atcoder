def check_substring(S, target):
    p = 0
    for s in S:
        if s == target[p]:
            p += 1
            if p == len(target):
                return p
    return p


n, t = input().split()
data = []
for i in range(int(n)):
    s = input()
    f = check_substring(s, t)
    r = check_substring(s[::-1], t[::-1])
    data.append((f, r))

# fの値に基づいて降順にソート
data.sort(key=lambda x: x[0], reverse=True)

count = 0

for i in range(len(data)):
    # 各列とペアを組むために必要なfの最小値を計算
    min_required_f = max(0, len(t) - data[i][1])

    # 二分探索を使用して必要なfの位置を見つける
    l, r = 0, i - 1
    while l <= r:
        mid = (l + r) // 2
        if data[mid][0] >= min_required_f:
            l = mid + 1
        else:
            r = mid - 1

    count += (i - r)  # 必要なf以上の列の数をカウント

print(count)
