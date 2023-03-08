class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
obj=doublelinkedlist()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
obj.insert_end()
obj.display()
