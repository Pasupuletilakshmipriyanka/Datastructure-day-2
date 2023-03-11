class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next.prev=prev
        temp.next=None
        temp.prev=None
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
obj.display()
obj.delete_position(2)
print("\n")
obj.display()
