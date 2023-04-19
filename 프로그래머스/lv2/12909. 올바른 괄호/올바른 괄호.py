def solution(s):
    stack = []
    for i in s:
        # (면 무조건 append
        if i == '(':
            stack.append(i)
        # )인데 스택이 비어있으면 False
        else:
            if len(stack) > 0:
                if stack.pop() != '(':
                    return False
            else:
                return False
    
    if len(stack) != 0:
        return False
    
    return True