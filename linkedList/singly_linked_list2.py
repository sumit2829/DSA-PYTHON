class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
            
    # insert at begin
    def insert_begin(self,data):
        # create a node
        newNode = Node(data)
        
        # if linkedlist is empty so new node will tail,head all
        if (self.head is None):
            self.head = newNode
            self.tail = newNode
            return
        
        # newNode refer to head 
        newNode.next = self.head
        # head go to newnode
        self.head = newNode
        
    def insert_end(self,data):
        # creating node
        newNode = Node(data)
        #  if linkedlist is empty so newnode will tail head and all
        if (self.head is None):
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode
        
    def deleteBegin(self):
        if self.head is None:
            print("Linked List is empty") 
            return
        self.head = self.head.next
        
    def deleteEnd(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        
    def delete_value(self,value):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next is None:
            print("value not found")
            return
        temp.next = temp.next.next
             
    def searchNode(self,key):
        temp = self.head
        position = 0
        
        while temp:
            if temp.data == key:
                return position
            temp = temp.next
            position +=1
        return -1
    
    def countNode(self):
        count = 0
        temp = self.head
        
        while temp:
            count +=1
            temp = temp.next
        return count 
    
    def reverse(self):
        prev = None
        curr = self.head
        self.tail = self.head
        
        while curr:
            next_Node = curr.next
            curr.next = prev
            prev = curr
            curr = next_Node
        self.head = prev
        
    def display(self):
        if self.head is None:
            print("Linked List Is Empty") 
            return 
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
        
    def FindMiddle(self):
        slow = self.head
        fast = self.head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
ll = LinkedList()

ll.insert_begin(10)
ll.insert_begin(20)
ll.insert_begin(40)
ll.insert_end(30)

print("Middle:", ll.FindMiddle())
print("Count:", ll.countNode())

ll.reverse()

ll = LinkedList()

ll.insert_begin(10)
ll.insert_begin(20)
ll.insert_begin(40)
ll.insert_end(30)
ll.display()

print("Middle:", ll.FindMiddle())
print("Count:", ll.countNode())



ll.reverse()

ll.display()

ll.deleteEnd()
ll.display()
ll.deleteBegin()

ll.display()


        