class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       word4=''
       for i in range(max(len(word1),len(word2))):
        if i<len(word1):
            word4+=word1[i]
        if i<len(word2):
            word4+=word2[i]

       return word4
       
        