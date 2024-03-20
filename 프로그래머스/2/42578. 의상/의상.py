def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict.keys():
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 1
    
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    # (얼굴 + 입지 않는 경우) * (상의 + 입지 않는 경우) * (하의 + 입지 않는 경우) - 아무것도 입지 않는 경우
    # (2+1)*(1+1)*(1+1)-1 = 11
    
    answer = 1
    for type in dict:   
        answer *= (dict[type] + 1)
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1
