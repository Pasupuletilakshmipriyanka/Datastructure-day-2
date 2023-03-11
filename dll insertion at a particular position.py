class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos):
        n=Node(400)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
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
n3=Node(300)
n3.prev=n2
n2.next=n3
obj.insert_pos(1)
obj.display()
