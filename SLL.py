class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_from_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next

    def delete_from_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def search(self, key):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1
        return -1

# Testing
s = SinglyLinkedList()
s.insert_at_beginning(100)
s.insert_at_beginning(200)
s.insert_at_end(300)
s.display()