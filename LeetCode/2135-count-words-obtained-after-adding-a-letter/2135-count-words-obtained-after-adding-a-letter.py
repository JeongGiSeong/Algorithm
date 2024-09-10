# startword: [g, j], targetword: [jg] 이걸 1번으로 쳐야된다는건가?
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWordSet = set(''.join(sorted(word)) for word in startWords)
        # targerWordSet을 만들지 않는 이유: 순서가 다른 단어가 정렬되면 같은 단어로 인식되기 때문
        count = 0

        for targetWord in targetWords:
            sortedTarget = ''.join(sorted(targetWord))
            for i in range(len(sortedTarget)):
                # targetWord에서 1개를 뺀 문자열이 startWordSet에 있는지 확인
                modifiedTarget = sortedTarget[:i] + sortedTarget[i+1:]
                if modifiedTarget in startWordSet:
                    count += 1
                    break

        return count
        
####################### 시간 초과 ######################
# class Solution:
#     def check(self, startWord: str, targetWord: str)-> bool:
#         if len(startWord) != len(targetWord)-1:
#             return False
#         for s in startWord:
#             if s not in targetWord:
#                 return False
#         return True


#     def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
#         ans = 0
#         targetWords.sort()
#         startWords.sort()
#         for targetWord in targetWords:
#             for startWord in startWords:
#                 if self.check(startWord, targetWord):
#                     ans += 1 
#                     break

#         return ans
