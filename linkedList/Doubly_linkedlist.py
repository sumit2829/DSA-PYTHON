class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def insert_end(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = newNode
        newNode.prev = temp

    def display_forward(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def display_backward(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


dl = DoublyLinkedList()

dl.insert_begin(10)
dl.insert_begin(40)
dl.insert_end(20)
dl.insert_begin(30)

print("Forward:")
dl.display_forward()

print("Backward:")
dl.display_backward()