def calc(s1, s2, s3):
    m = len(s1)
    min_time = 10000

    # s1を基準に考える
    for i in range(m):
        char = s1[i]
        idxs_s2 = [idx for idx, c in enumerate(s2) if c == char]
        idxs_s2 += [idx + k*m for idx in idxs_s2 for k in range(1, 3)]
        idxs_s3 = [idx for idx, c in enumerate(s3) if c == char]
        idxs_s3 += [idx + k*m for idx in idxs_s3 for k in range(1, 3)]
        if not idxs_s2 or not idxs_s3:
            continue

        for idx_s2 in idxs_s2:
            for idx_s3 in idxs_s3:
                if i != idx_s2 and i != idx_s3 and idx_s2 != idx_s3:
                    time = max(i, idx_s2, idx_s3)
                    min_time = min(min_time, time)

    return min_time


m = int(input())
s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

result = calc(s1, s2, s3)
if result == 10000:
    result = -1
print(result)
