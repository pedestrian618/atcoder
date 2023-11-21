S = input()
flag = 0
R = []
for s in S:
    if s == 'A':
        flag = 1
    elif s == 'B' and flag == 1:
        flag = 2
    elif s == 'C' and flag == 2:
        flag = 0
        del R[-2:]
        if len(R) > 1 and R[-2:] == ['A', 'B']:
            flag = 2
        elif len(R) > 0 and R[-1] == 'A':
            flag = 1
        continue
    else:
        flag = 0
    R.append(s)
print(''.join(R))
