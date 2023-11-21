import sys
input = sys.stdin.readline
N, T = input().split()
N = int(N)


def is_similar(str1, str2):
    len1, len2 = len(str1), len(str2)
    diff = abs(len1 - len2)

    # 文字列の長さが2以上異なる場合
    if diff > 1:
        return False

    # 文字列の長さが同じ場合
    if diff == 0:
        count_diff_char = sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)
        return True if count_diff_char <= 1 else False

    # str1がstr2より1文字多い場合
    if len1 > len2:
        str1, str2 = str2, str1

    # 1文字だけ異なる場合のチェック
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return True if str1[i:] == str2[i+1:] else False
    return True


O = []
for n in range(N):
    S = input().strip()
    if is_similar(S, T):
        O.append(n+1)
print(len(O))
print(*O)
