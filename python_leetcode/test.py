class Test:
    def __init__(self, data):
        self.data1 = data
        self.data2 = data * 2
        self.list = [data, data*2, data*3]
        self.set = {data, data*2, data, data**2}
    def print(self):
        print("args1:", self.data1)
        print("args2:", self.data2)
        print("list:", self.list )
        print("set:", self.set)
    def swap(self):
       self.data1, self.data2 = self.data2, self.data1
    def dataMapping(self):
        self.list = list(map(lambda x: x*2, self.list))
    def popElement(self, index):
        self.list[index], self.list[index - 1] = self.list[index - 1], self.list[index]
my = Test(10)

my.print()
my.popElement(1)
my.print()



