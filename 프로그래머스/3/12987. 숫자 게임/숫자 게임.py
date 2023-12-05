# 최대한 차이가 적게 이기고, 차이가 많게 져야됨
# 일일히 루프 돌면서 찾는 건 O(n^2)이라 시간 초과
# 내림차순 정렬 후 B[0] 보다 작은 A가 나오면 승점+1 하고 B[0] 삭제
def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    for a in A:
        if a < B[0]:
            answer += 1
            del B[0]
    return answer