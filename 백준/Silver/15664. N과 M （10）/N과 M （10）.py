import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


########### 백트래킹 풀이 #############
n,m = map(int,input().split())
array = list(map(int, input().split()))
array.sort()
visited = [False] * n
s = []
 
def dfs(depth: int, start: int):
# 지역변수 prev가 마지막 수를 기억해서 중복을 방지한다.
    prev = 0
    if depth==m:
        print(' '.join(map(str,s)))
        return
    for i in range(start, n):
        if not visited[i] and array[i] != prev:
            visited[i] = True
            s.append(array[i])
            prev = array[i]
            dfs(depth+1, i+1)
            visited[i] = False
            s.pop()
    
dfs(0, 0)
