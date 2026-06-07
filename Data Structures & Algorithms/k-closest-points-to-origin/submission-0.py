import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        c=[]
        d=[]
        for i in range(len(points)):
            a,b=heapq.heappop(points)
            c.append([a*a + b*b,a,b])
        heapq.heapify(c)
        for _ in range(k):
            x=heapq.heappop(c)
            d.append([x[1],x[2]])
        return d

       