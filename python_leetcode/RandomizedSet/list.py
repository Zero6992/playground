import random
class RandomizedSet:
    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.list) # val: index
            self.list.append(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.dict:
            lastValue = self.list[-1]
            self.dict[lastValue] = self.dict[val]
            self.list[self.dict[val]] = lastValue
            del self.list[-1]            
            del self.dict[val]
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(self.list)


myRandom = RandomizedSet()


myRandom.insert(0)
myRandom.insert(1)
myRandom.remove(0)
myRandom.insert(2)
myRandom.remove(1)

for i in range(10):  
    print(myRandom.getRandom())