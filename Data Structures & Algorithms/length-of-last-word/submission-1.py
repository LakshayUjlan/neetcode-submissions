class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for c in s[::-1]:
            if c != " ":
                count+=1
            if count > 0:
                if c == " ":
                    return count
        return count


        