import sys

read = sys.stdin.readline



T = int(read())
for _ in range(T):
    문자열 = read().strip()
    리스트 = []
    flag = False
    if 문자열[0] == ')':
        flag = True # NO

    for s in 문자열:
        if s == '(':
            리스트.append(s)
        else:
            if len(리스트) == 0:
                flag = True # NO
            else:
                리스트.pop()

    if flag:
        print("NO")
    elif len(리스트) == 0:
        print("YES")
    else:
        print("NO")