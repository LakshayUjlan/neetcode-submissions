class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      if not digits:
        return []
      a={
        "2":"abc" , "3":"def" , "4":"ghi" , "5":"jkl" , "6":"mno" ,
        "7":"pqrs" , "8":"tuv" , "9":"wxyz"
        }
      res=[]
      def somthn(k,curr):
            if k == len(digits):
                res.append(curr)
                return
            for ch in a[digits[k]]:
                somthn(k+1,curr+ch)
      somthn(0,"")
      return res

    
      
        
        



