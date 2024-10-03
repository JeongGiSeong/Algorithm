import sys
input = sys.stdin.readline

array = []
for i in range(41):
    array.append(2**i)

for _ in range(int(input())):
    hp, food = map(int, input().split())

    tmp = 0
    for i in range(41):
        if hp >= array[i]:
            tmp = i + 1

    print(tmp+food)