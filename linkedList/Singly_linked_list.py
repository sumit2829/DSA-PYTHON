class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_begin(self,data):
        #creating Node
        
        newNode = Node(data)
        
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = self.head
        self.head = newNode
        
    def insert_at_position(self, data, pos):
        new_node = Node(data)

        # Insert at beginning
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 0

        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node
                
        
    def display(self):

        if self.head is None:
            print("Linked List is Empty !!")
            return

        temp = self.head

        while temp:
            print(temp.data, end =" -> ")
            temp = temp.next

        print("None")
    
        
ll = LinkedList()
print("insert")
ll.insert_begin(10)
ll.insert_begin(20)
ll.insert_begin(30)
ll.insert_at_position(11, 1)
ll.display()
        
        
        
        