import sys

input = sys.stdin.readline

books = {}
for _ in range(int(input())):
    book = input().strip()

    if book in books:
        books[book] += 1
    else:
        books[book] = 1
    
m = max(books.values())

answer = []
for k, v in books.items():
    if v == m:
        answer.append(k)

print(sorted(answer)[0])