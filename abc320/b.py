def pali(s: str) -> bool:
    return s == s[::-1]


def calc(s: str) -> int:
    n = len(s)
    max_length = 1
    for i in range(n):
        for j in range(i + 1, n):
            if pali(s[i:j+1]) and j-i+1 > max_length:
                max_length = j-i+1

    return max_length


S = input().strip()
print(calc(S))
