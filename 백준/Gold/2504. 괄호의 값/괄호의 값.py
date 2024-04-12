s = input()
stack = []
ans = 0
tmp = 1

for i in range(len(s)):
    if s[i] == '(':
        tmp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if s[i-1] == '(':
            ans += tmp
        tmp //= 2
        stack.pop()
    elif s[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if s[i-1] == '[':
            ans += tmp
        tmp //= 3
        stack.pop()

if stack:
    ans = 0

print(ans)
