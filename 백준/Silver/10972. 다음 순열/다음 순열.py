import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


# DFS 사용 -> 런타임 에러(재귀 깊이)
# ****** 파이썬의 재귀 깊이는 최대 1000 ******
# 해당 문제에서 N은 최대 10000까지 가므로 재귀 깊이 에러가 발생

# n = int(read())
# array = list(map(int, read().split()))
# sorted_array = sorted(array)
# s = []
# visited = [False] * n
# ans_list = []

# def dfs(depth: int):
#     if depth == n:
#         ans_list.append(' '.join(map(str, s)))
#     for i in range(n):
#         # 방문하지 않은 경우
#         if not visited[i]:
#             visited[i] = True
#             s.append(sorted_array[i])
#             dfs(depth + 1)
#             s.pop()
#             visited[i] = False


# dfs(0)
# # print(*ans_list, sep='\n')
# index = ans_list.index(' '.join(map(str, array)))
# if index + 1 == len(ans_list):
#     print(-1)
# else:
#     print(ans_list[index + 1])

#######################################################

# next permutation 알고리즘
# [2 1 4 3]
# (1) 뒤에서부터 앞 값과 비교해서 앞값보다 큰 수를 타겟으로 잡음
# 1 < 4 이므로 타겟은 1
# 타겟을 찾았으면 타겟 뒤 [4, 3]부터 다시 검사
# (2) 타겟인 1보다 더 큰 수를 찾는다. -> 3
# (3) 타겟과 3 swap -> [2 3 4 1]
# (4) 기존 타겟 자리까지 수 [2 3]을 제외한 [4 1]을 정렬한다
# -> [2 3 ~]으로 시작하는 순열이기 때문에 가장 작은 순열을 위해 정렬하는 것
# 그럼 2 3 1 4가 되고 이게 다음 순열이 된다.

n = int(read())
permut = list(map(int, read().split()))

# (1)번 과정
for i in range(n - 1, 0, -1):
    if permut[i - 1] < permut[i]:
        target = i - 1
        break
# break가 한 번도 실행되지 않았으면 마지막 순열이라는 의미
else:
    print(-1)
    exit()

# (2)번 과정
for i in range(n - 1, 0, -1):
    # (3)번 과정
    if permut[target] < permut[i]:
        permut[target], permut[i] = permut[i], permut[target]
        #(4)번 과정
        permut = permut[:target + 1] + sorted(permut[target + 1:])
        break

print(*permut)