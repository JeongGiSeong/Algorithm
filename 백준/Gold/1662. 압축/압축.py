import sys
input = sys.stdin.readline

S = input().strip()
cur = 0
stack = []

for c in S:
    if c == '(':
        # 반복 횟수와 현재 길이를 스택에 저장
        stack.append([int(tmp_repeat), cur - 1])
        cur = 0 # 현재 길이 초기화
    elif c == ')':
        repeat, prev = stack.pop()
        cur = repeat * cur + prev
    else:
        cur += 1
        tmp_repeat = c
print(cur)