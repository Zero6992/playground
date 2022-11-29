class Test:
    def __init__(self, data):
        self.data1 = data
        self.data2 = data * 2
        self.list = [data, data*2, data*3]
    def print(self):
        print("args1:", self.data1)
        print("args2:", self.data2)
        print("list:", self.list )
    def swap(self):
       self.data1, self.data2 = self.data2, self.data1
    def dataMapping(self):
        self.list = list(map(lambda x: x*2, self.list))
my = Test(10)

my.print()
my.dataMapping()
my.print()


