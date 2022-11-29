class listNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

class lnkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    def addNode(self, node):
        if not isinstance(node, listNode): # 判斷item是否為node
            node = listNode(node)
        
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            
        self.tail = node
        return
    def allNode(self):
        if self.head is None:
            print("There is no node inside!")
        while(1):
            if self.head is not None:
                print(self.head.data)
            else:
                return
            self.head = self.head.next

list1 = lnkedList()
list1.addNode(10)
list1.addNode(12)
list1.addNode(12)
list1.addNode(13)

list1.allNode()