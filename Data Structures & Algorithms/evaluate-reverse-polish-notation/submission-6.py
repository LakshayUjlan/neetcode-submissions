import operator
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        dic ={"+":operator.add,"-":operator.sub,"*":operator.mul,"/": lambda a, b: int(a / b)}
        for a in tokens:
            if a not in dic:
                stack.append(int(a))
            else:
                c=stack.pop()
                d=stack.pop()
                stack.append(dic[a](d,c))
        return int(stack[0])


