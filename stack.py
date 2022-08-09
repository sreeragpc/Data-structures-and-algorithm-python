class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Stack:
    def __init__(self):
        self.head = None
    def isempty(self):
        if self.head == None:
            return True
        else :
            return False
    def push(self,data):
        if self.head == None :
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.ref = self.head
            self.head = newnode
    def pop(self):
        if self.head == None:
            print("there is no element to pop")
        else:
            self.head = self.head.ref
    def display(self):
        if self.head == None:
            print("stack is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data," _ ",end =" ")
                n = n.ref
newstack = Stack()
newstack.push(10)
newstack.push(58)
newstack.push(76)
newstack.push(154)
newstack.pop()
newstack.display()



