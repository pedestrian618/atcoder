def find_subsequence(s, target):
    idx, j = 0, 0
    for i in range(len(s)):
        if s[i] == target[j]:
            j += 1
            if j == len(target):
                return idx + 1
        else:
            if j == 0:
                idx += 1
    return -1  # not found


strings = ["abba", "bcb", "aaca"]
target = "bac"

for s in strings:
    position = find_subsequence(s, target)
    if position != -1:
        print(
            f"'{target}' is a subsequence of '{s}' up to the {position}th character.")
    else:
        print(f"'{target}' is not a subsequence of '{s}'.")
