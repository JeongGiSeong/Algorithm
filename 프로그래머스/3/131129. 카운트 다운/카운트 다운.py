def solution(target):
    scoreTable = [[0, 0] for _ in range(max(70, target)+1)]
    for i in range(1, 21):
        scoreTable[i] = [1, 1]  # 1~20: 싱글
    for i in range(21, 41):
        scoreTable[i] = [1, 0]  # 21~40: 더블, 트리플
    for i in (23, 25, 29, 31, 35, 37):
        scoreTable[i] = [2, 2]  # 23, 25, 29, 31, 35, 37: 싱글 두 번
    for i in range(41, 50):
        scoreTable[i] = [2, 1]  # 41~49: 싱글+더블
    scoreTable[50] = [1, 1]  # 50: 불 영역
    for i in range(52, 71):
        scoreTable[i] = [2, 2]  # 52~70: 싱글 두 번
    for i in range(42, 61, 3):
        scoreTable[i] = [1, 0]  # 42~60: 트리플
    
    for i in range(71, target+1):
        triple_20 = i - 60
        bull = i - 50
        is_triple_better = False
        if scoreTable[triple_20][0] < scoreTable[bull][0]:  # 트리플 20이 더 적은 다트를 사용하는 경우
            is_triple_better = True
        elif scoreTable[triple_20][0] == scoreTable[bull][0]:  # 다트 수가 같은 경우
            if scoreTable[bull][1] < scoreTable[triple_20][1]:  # 트리플 20이 더 많은 싱글 또는 불을 맞추는 경우
                is_triple_better = True
        if is_triple_better:
            scoreTable[i] = [scoreTable[triple_20][0] + 1, scoreTable[triple_20][1]]
        else:
            scoreTable[i] = [scoreTable[bull][0] + 1, scoreTable[bull][1] + 1]
    
    return scoreTable[target]
