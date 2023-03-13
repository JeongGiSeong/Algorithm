import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


########### 백트래킹 풀이 #############
n,m = list(map(int,input().split()))
 
s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        s.append(i)
        dfs(i)
        s.pop()
 
dfs(1)