class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # 단어를 집합으로 변환하여 중복 제거
        words = set(words)
        
        # 각 단어의 접미사를 해시테이블에서 제거
        for word in list(words):
            for k in range(1, len(word)):
                words.discard(word[k:])
        
        # 최종 참조 문자열의 길이 계산
        return sum(len(word) + 1 for word in words)