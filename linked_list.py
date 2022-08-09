
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def reverse(self):
        k = None
        n = self.head
        while n is not None :
            temp = n.ref
            n.ref = k
            k = n
            n = temp
        self.head = k     

f = LinkedList()
f.add_begin(10)
f.add_begin(20)
f.add_begin(30)
f.display()
f.reverse()
print("-------------------")
f.display()



             


