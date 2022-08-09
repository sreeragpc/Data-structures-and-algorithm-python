class Node:
    def __init__(self,data):
        self.data = data
        self.ref =  None    
class LinkedList:
    def __init__(self):
        self.head = None   
    def print_LL(self):
        if  self.head == None:
            print("LInked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end = " ")
                n = n.ref 
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node 
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print(x," node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node 

    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node 
        n = self.head
        while n.ref is not None:
            if n.ref.data == x :
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node 
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LInked list is not empty")
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty so can't delete nodes")
        else:
            self.head =  self.head.ref
    def delete_end(self):
        if self.head is None:
            print("linked list is empty so can't delete nodes")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    def delete_by_value(self,x):
        if self.head is None:
            print("can't delete linked list is empty")
            return        
        if x == self.head:
            self.head = self.head.ref
            return
        if self.head is not None:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Nod is not present") 
            else:
                n.ref = n.ref.ref



                        
LL1 = LinkedList()
LL1.add_begin("pc")
LL1.add_begin("sreerag")
LL1.add_end("python")
LL1.add_end("backend developer")
# LL1.add_begin(80)
# LL1.add_after(1000,500)
# LL1.add_before(2000,100)
# LL1.delete_begin()
# LL1.delete_end()
# LL1.delete_by_value(2000)
LL1.print_LL()


# LL2 = LinkedList()

# LL2.insert_empty(100)
# LL2.print_LL()

# LL3 = LinkedList()
# LL3.delete_begin
# LL3.print_LL

# LL4 = LinkedList()
# LL4.delete_begin