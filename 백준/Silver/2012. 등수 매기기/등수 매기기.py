import sys
input = sys.stdin.readline

N = int(input())
rank = list(int(input()) for _ in range(N))
rank.sort()

discontent = 0 
for i in range(N):
    if rank[i] != i+1: # 자기 예상 등수와 실제 등수가 다르면
        discontent += abs(rank[i]-(i+1))
print(discontent)
