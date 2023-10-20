보, 설치 = 1, 1
기둥, 삭제 = 0, 0

def isImpossible(answer):
    for x, y, a in answer:
        if a == 기둥: # 기둥일 때
            if y != 0 and (x, y-1, 기둥) not in answer and \
        (x-1, y, 보) not in answer and (x, y, 보) not in answer:
                return True
        else: # 보일 때
            if (x, y-1, 기둥) not in answer and (x+1, y-1, 기둥) not in answer and \
        not ((x-1, y, 보) in answer and (x+1, y, 보) in answer):
                return True
    return False

def solution(n, build_frame):
    answer = set()
    
    for x, y, a, b in build_frame:
        item = (x, y, a)
        
        if b == 설치: # 설치
            answer.add(item)
            if isImpossible(answer):
                answer.remove(item)
        else: # 삭제
            answer.remove(item)
            if isImpossible(answer):
                answer.add(item)
        # print(answer, sep='\n')
                
    answer = list(map(list, answer))
    answer.sort()
    
    return answer