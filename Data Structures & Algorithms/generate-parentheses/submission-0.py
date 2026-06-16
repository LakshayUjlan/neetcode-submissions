class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        subset=[]
        def par(opens,close):
          if len(subset)==n*2:
            res.append("".join(subset))
            return
          if opens < n:
            subset.append("(")
            par(opens+1,close)
            subset.pop()
          if close < opens:
            subset.append(")")
            par(opens,close+1)
            subset.pop()
        par(0,0)
        return res
          

          

        


    






             
          
