import re
N = int(input())
S = input()

if re.search('ab', S) or re.search('ba', S):
    print('Yes')
else:
    print('No')
