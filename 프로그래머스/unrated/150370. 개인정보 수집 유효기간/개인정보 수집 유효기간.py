def str2date(s):
    y, m, d = map(int, s.split('.'))
    return y*12*28 + m*28 + d

def solution(today, terms, privacies):
    item = dict()
    answer = []
    today = str2date(today)
    for term in terms:
        약관, 유효기간 = term.split()
        item[약관] = int(유효기간)
        
    for idx, privacie in enumerate(privacies, 1):
        수집일, 약관 = privacie.split()
        수집일 = str2date(수집일)
        
        if today >= 수집일 + (item[약관] * 28):
            answer.append(idx)
        
    return answer
    
    