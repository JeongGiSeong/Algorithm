# 완전탐색으로 한다면? 순열을 사용해서?
# 50 P 25 -> 무조건 시간초과

name = input()

cnt = {}
for a in name:
    if a not in cnt:
        cnt[a] = 1
    else:
        cnt[a] += 1

def is_palindrome(name):
    # 길이가 짝수면 모든 요소의 개수가 짝수여야 함    
    if len(name) % 2 == 0:
        for value in cnt.values():
            if value % 2 != 0:
                return False
    # 길이가 홀수인 경우, 하나의 문자만 홀수 개 있어야 함
    else:
        odd_count = 0
        for value in cnt.values():
            if value % 2 != 0:
                odd_count += 1
            if odd_count > 1:
                return False
    return True

# is_palindrome()으로 팰린드롬의 가능성은 확실.
# 사전 순으로 돌면서 첫 팰린드롬을 출력하면 됨
def get_palindrome(name):
    ans = ''
    if is_palindrome(name):
        odd_alpha = ''
        for k, v in sorted(cnt.items()):
            ans += k * (v // 2)
            if v % 2 != 0:
                odd_alpha = k
        return ans + odd_alpha + ans[::-1]
    else:
        return "I'm Sorry Hansoo"


print(get_palindrome(name))