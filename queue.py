class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Queue:
    def __init__(self):
        self.head = self.rear = None
    def enqueue(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = self.rear = newnode
        else:
            self.rear.ref = newnode
            self.rear = newnode
    def dequeue(self):
        if self.head == None:
            print("There is nothing to dequeue") 
        else:
            self.head = self.head.ref             
    def display(self):
        if self.head == None :
            print("queue is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref

new = Queue()
new.enqueue(100)
new.enqueue(25)
new.enqueue(56)
new.enqueue(85)
new.display()
