cache = [-1] * 91
cache[0] = 0
cache[1] = 1

def fibo(n):
    if cache[n] == -1:
        cache[n] = fibo(n - 1) + fibo(n - 2)
    
    return cache[n]

print(fibo(int(input())))