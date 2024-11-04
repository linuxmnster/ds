class Node:   
    def __init__(self,data):   
        self.data = data   
        self.next = None      

class SinglyLinkedList:    
    def __init__(self):   
        self.head = None   
        self.tail = None   

    def addNode(self, data):   
        newNode = Node(data)   
        if(self.head == None):     
            self.head = newNode  
            self.tail = newNode   
        else:    
            self.tail.next = newNode   
            self.tail = newNode   

    def display(self):   
        current = self.head   
        if(self.head == None):   
            print("List is empty")   
            return;   
        print("Nodes of singly linked list: ")   
        while(current != None):    
            print(current.data)   
            current = current.next 

sList = SinglyLinkedList()   
  
sList.addNode(1)   
sList.addNode(2)   
sList.addNode(3)   
sList.addNode(4)   
  
sList.display()
