def solution(phone_book):
    hash_map = {} # 해시맵 생성
    for phone_number in phone_book: # 전화번호부의 각 전화번호에 대해
        hash_map[phone_number] = 1 # 해시맵에 전화번호 저장
    
    for phone_number in phone_book: # 전화번호부의 각 전화번호에 대해
        jubdoo = "" # 접두사 초기화
        for number in phone_number: # 각 번호에 대해
            jubdoo += number # 접두사 생성
            if jubdoo in hash_map and jubdoo != phone_number: # 만약 접두사가 해시맵에 있고 현재 전화번호와 다르다면
                return False # False 반환
    return True # 모든 전화번호를 반복한 후 True 반환

# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
#             return False
#     return True