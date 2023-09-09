def can_fit_in_M_lines(words, W, M):
    current_width = 0
    used_lines = 1
    for word in words:
        if current_width == 0:
            current_width += word
        else:
            current_width += 1 + word

        if current_width > W:
            used_lines += 1
            current_width = word

    return used_lines <= M


def find_min_width(words, M):
    left = max(words)
    right = sum(words) + len(words) - 1

    while left < right:
        mid = (left + right) // 2
        if can_fit_in_M_lines(words, mid, M):
            right = mid
        else:
            left = mid + 1

    return left


N, M = map(int, input().split())
L = list(map(int, input().split()))
print(find_min_width(L, M))
