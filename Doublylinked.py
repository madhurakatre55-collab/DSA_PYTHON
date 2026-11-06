class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.prev = None
        
class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <->")
            temp = temp.next
        print("None")
    def display_reverse(self):
        temp = self.head
        if not head:
            return 
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data,end="<->")
            temp = temp.prev
        print("None")
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = self
            