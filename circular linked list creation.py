class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class createlist:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    def add(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head   
    def display(self):
        current=self.head
        if self.head is None:
            print("Linked List is empty")
        else:
            print("Nodes of the circular linked list:")
            print(current.data,"-->")
            while(current.next!=self.head):
                if self.head is None:
                    print("List is empty")
                    return
                else:
                    print("Nodes of the circular linked list:")
                    print(current.data,"-->")
                    while(current.next!=self.head):
                        current=current.next
                        print(current.data,"-->")
class circularlinkedlist:
    c1=createlist()
    c1.add("S")
    c1.add("M")
    c1.add("I")
    c1.add("L")
    c1.add("E")
    c1.display()
                    
                  
            
