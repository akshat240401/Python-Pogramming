from tkinter.messagebox import NO
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Sl:
    def __init__(self):
        self.head=None
    
    def travsersal(self):
        if self.head is None:
            print("Singly Linked List Is Empty !!!")
        else:
            a=self.head
            while a is not None:
                print(a.data ,end=" ")
                a=a.next
    
    def insert_at_beginning(self,data):
        print()
        nb=Node(data)
        nb.next=self.head
        self.head=nb

n1=Node(5)  
singly=Sl()
singly.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4

singly.insert_at_beginning(2)
singly.travsersal()