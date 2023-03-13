import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


########### 백트래킹 풀이 #############
n,m = map(int,input().split())
array = list(map(int, input().split()))
array.sort()
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in array:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
    
dfs()