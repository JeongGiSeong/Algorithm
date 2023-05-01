def solution(n, costs):
    # 비용을 오름차순으로 정렬
    costs.sort(key=lambda x: x[2])
    # 연결된 노드 추적
    connection = [costs[0][0]]
    # 최종 답안 초기화
    answer = 0
    # 모든 노드가 연결될 때까지 반복
    while len(connection) != n:
        for i, cost in enumerate(costs):
            # 이미 연결된 경우 건너뛰기
            if (cost[0] in connection) and (cost[1] in connection):
                continue
            # 하나의 노드만 연결된 경우
            if (cost[0] in connection) or (cost[1] in connection):
                # 비용 추가
                answer += cost[2]
                # 연결된 노드 추가
                connection.append(cost[0])
                connection.append(cost[1])
                # 중복 제거
                connection = list(set(connection))
                # 사용한 간선 제거
                costs[i] = [-1, -1, -1]
                break
    return answer