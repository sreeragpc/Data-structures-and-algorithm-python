class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None   
class DLinkedList:
    def __init__(self):
        self.head = None 
    def print_LL(self):
        if  self.head == None:
            print("LInked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end = " ")
                n = n.nref 
    def print_LL_R (self):
        if  self.head == None:
            print("LInked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref                 
            while n is not None:
                print(n.data,"-->",end = " ")
                n = n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list is not empty")  
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    def add_after(self,data,x):
        if self.head is None:
            print("linked list is null")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present ")
            elif n.nref is None:
                new_node = Node(data)
                n.nref = new_node
                new_node.pref = n
            else:
                new_node = Node(data)
                n.nref.pref = new_node
                new_node.nref = n.nref
                n.nref = new_node
                new_node.pref = n

    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is Empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node            
            return
        n = self.head
        while n.nref is not None:
            if x == n.nref.data:
                break
            n = n.nref
        if n.nref is None:
            print("Given Node is not presnt in Linked List!")
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node            
            n.nref = new_node




                        




dll = DLinkedList()
dll.add_begin(10)
dll.add_end(25)
dll.add_after(100,10)
dll.add_before(1,25)
print("--------")
dll.print_LL()
print("\n reverse")
dll.print_LL_R()    

             

            
