import sys
input = sys.stdin.readline

array = [2**i for i in range(41)]

def find_max_power(hp):
    for i in range(41):
        if hp < array[i]:
            return i
    return 41

for _ in range(int(input())):
    hp, food = map(int, input().split())
    print(find_max_power(hp) + food)
