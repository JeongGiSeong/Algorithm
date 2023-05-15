from collections import deque

def solution(begin, target, words):
    # target이 words에 없으면 변환할 수 없으므로 0을 반환
    if target not in words:
        return 0

    # 두 단어가 한 번의 변환으로 서로 변환 가능한지 여부를 반환하는 함수
    def can_transform(word1, word2):
        diff = 0
        for a, b in zip(word1, word2):
            if a != b:
                diff += 1
        return diff == 1

    # BFS 알고리즘을 사용하여 최소 단계 수를 찾음
    queue = deque([(begin, 0)])
    visited = set()
    while queue:
        current_word, count = queue.popleft()
        if current_word == target:
            return count
        for word in words:
            # 방문하지 않은 단어 중에서 한 번의 변환으로 변환 가능한 단어를 찾음
            if word not in visited and can_transform(current_word, word):
                # 큐에 추가하고 방문 표시
                queue.append((word, count + 1))
                visited.add(word)
    return 0