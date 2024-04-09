from sys import stdin
input = stdin.readline

def check(s):
    stk = []

    for c in s:
        if c == '(' or c == '[':
            stk.append(c)
        elif c == ')':
            if not stk or stk[-1] != '(':
                return False
            stk.pop()
        elif c == ']':
            if not stk or stk[-1] != '[':
                return False
            stk.pop()
    
    return len(stk) == 0

while True:
    s = input().replace("\n", "")
    if s == '.':
        break
    print('yes' if check(s) else 'no')