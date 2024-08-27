import sys
input = sys.stdin.readline

N = int(input()) # 1 <= N <= 100,000
S = input()

# 연속으로 치킨을 먹는 날의 최댓값을 가장 작게 만드는 방법
# 시간복잡도: O(N log N) 이하
# 정답 = N/(N-C개수+1)

print(int(N / (N - S.count('C') + 1)))