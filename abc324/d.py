from collections import Counter


def is_permutation(s_count, num_str):
    return Counter(s_count) == Counter(num_str)


def square_permutations_count(S, zero_count):
    # 生成できる最大の整数を考えて、その平方根を求める
    max_num = int('9' * len(S))
    max_sqrt = int(max_num**0.5) + 1

    count = 0
    s_count = Counter(S)

    for i in range(max_sqrt + 1):
        square_num = i * i
        if (len(S)-len(str(square_num))) <= zero_count:
            if is_permutation(s_count, "0"*(len(S)-len(str(square_num))) + str(square_num)):
                count += 1

    return count


N = int(input())
S = input().strip()
s_count = Counter(S)
zero_count = s_count['0']
print(square_permutations_count(S, zero_count))
