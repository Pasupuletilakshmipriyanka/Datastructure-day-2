class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def delete_start(self):
        temp=self.head
        self.head=temp.next
        self.head.prev=None
        temp.next=None
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
obj.delete_start()
print("\n")
obj.display()
