class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None

    def push(self, data):
        newNode = Node(data)
        if self.val == None:
            self.val = newNode
        else:
            temp = self.val
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

    def pop(self):
        temp = self.val
        self.val = self.val.next
        return temp

class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data