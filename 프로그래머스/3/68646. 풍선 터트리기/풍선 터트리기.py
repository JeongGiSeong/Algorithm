def solution(a):
    # 리스트 중간에 있는 값은 자신 위치의 좌/우 리스트의 최솟값보다 작을 경우 생존 가능
    
    answer = [0 for _ in range(len(a))]
    minLeft, minRight = float("inf"), float("inf")
    for i in range(len(a)):
        if a[i] < minLeft:
            minLeft = a[i]
            answer[i] = 1
        if a[-1-i] < minRight:
            minRight = a[-1-i]
            answer[-1-i] = 1
    return sum(answer)