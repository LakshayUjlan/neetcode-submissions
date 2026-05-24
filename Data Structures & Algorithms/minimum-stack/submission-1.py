class MinStack:

    def __init__(self):
        self.a=[]
        
    def push(self, val: int) -> None:
        self.a.append(val)
    def pop(self) -> None:
        self.a.pop()
    def top(self) -> int:
        return self.a[-1]
    def getMin(self) -> int:
        mini=self.a[0]
        for b in self.a:
            if b<mini:
                mini=b
        return mini
            

