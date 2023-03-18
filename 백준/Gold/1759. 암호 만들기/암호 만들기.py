import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 각 줄에 사전식으로 가능성 있는 암호 전부 출력
# 3 ≤ L ≤ C ≤ 15

l, c = map(int, read().split())
alphabet = list(map(str, read().split()))
alphabet.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
stack = []

def dfs(depth, start):
    if depth == l:
        vowel = 0
        consonant = 0
        # 모음 1개 이상, 자음 2개 이상인지 검사
        for i in stack:
            if i in vowels:
                vowel += 1
            else:
                consonant += 1
        if vowel < 1 or consonant < 2:
            return
        print(*stack, sep='')
        return

    for i in range(start, c):
        stack.append(alphabet[i])
        dfs(depth + 1, i + 1)
        stack.pop()

dfs(0, 0)