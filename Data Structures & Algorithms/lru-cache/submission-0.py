class LRUCache:

    def __init__(self, capacity: int):
        self.lis={}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.lis:
            return -1

        value = self.lis[key]

        del self.lis[key]
        self.lis[key] = value

        return value

    def put(self, key: int, value: int) -> None:
       if key in self.lis:
        del self.lis[key]

       self.lis[key] = value
       if len(self.lis) > self.capacity:
        first_key = next(iter(self.lis))
        del self.lis[first_key]