def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    visited = []
    while True:
        if sum(answer) == n:
            return answer
        
        for i in range(n):
            progresses[i] += speeds[i]
        
        cnt = 0
        for i in range(n):
            if progresses[i] >= 100:
                if i not in visited:
                    visited.append(i)
                    cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)