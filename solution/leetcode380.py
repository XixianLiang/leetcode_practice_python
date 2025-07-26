import random


class RandomizedSet:

    def __init__(self):
        self.hash = dict()
        self.array = []

    def insert(self, val: int) -> bool:
        if self.hash.get(val, None) is not None:
            return False
        self.hash[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if self.hash.get(val, None) is None:
            return False
        idx = self.hash[val]
        if val != self.array[-1]:
            self.hash[self.array[-1]] = idx
            self.array[-1], self.array[idx] = self.array[idx], self.array[-1]
        self.hash[val] = None
        del self.array[-1]
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.array) - 1)
        r = self.array[idx]
        self.remove(r)
        return r


# Your RandomizedSet object will be instantiated and called as such:
# ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
# [[],[1],[2],[2],[],[1],[2],[]]
# ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
# [[],[0],[1],[0],[2],[1],[]]
obj = RandomizedSet()
print(obj.insert(0))
print(obj.insert(1))
print(obj.remove(0))
print(obj.insert(2))
print(obj.remove(1))
print(obj.getRandom())