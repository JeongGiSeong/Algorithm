def solution(n, lost, reserve):
    # 여벌 학생이 도난 학생일수도 있음. 조건 잘 확인할 것
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    # 왼쪽부터 확인? 왜?
    # -> 앞 원소부터 탐색하기 때문. 오른쪽부터 확인하려면 reversed 사용하면 됨.
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        # elif로 한 이유 : if로 하면 2명한테 빌려줄 수도 있음
        elif i+1 in set_lost:
            set_lost.remove(i+1)
            
    answer = n - len(set_lost)
    return answer