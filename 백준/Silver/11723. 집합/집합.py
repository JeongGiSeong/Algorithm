import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


# 11723번 집합
n = int(read())
bit = 0

for _ in range(n):
    command = read().split()

    if command[0] == "all":
        bit = (1 << 20) - 1
    elif command[0] == "empty":
        bit = 0
    else:
        op = command[0]
        num = int(command[1]) - 1

        # add
        if op == 'add':
            bit |= (1 << num)
        # remove
        elif op == 'remove':
            bit &= ~(1 << num)
        # check
        elif op == 'check':
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)
        # toggle
        elif op == 'toggle':
            bit = bit ^ (1 << num)