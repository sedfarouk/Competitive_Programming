class MyHashMap:

    def __init__(self):
        self.MyHashMap = {}
        

    def put(self, key: int, value: int) -> None:
        if key in self.MyHashMap:
            self.MyHashMap[key] = value
        else:
            self.MyHashMap[key] = value
        

    def get(self, key: int) -> int:
        if key in self.MyHashMap.keys():
            return self.MyHashMap[key]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.MyHashMap.keys():
            del self.MyHashMap[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)