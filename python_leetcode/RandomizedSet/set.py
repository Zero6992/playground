import random
class RandomizedSet:
    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(list(self.set))


myRandom = RandomizedSet()

for i in range(9, 100):
    myRandom.insert(i)
  
for i in range(10):  
    print(myRandom.getRandom())