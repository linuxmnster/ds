class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class Queue: 
    def __init__(self): 
        self.front = None 
        self.rear = None 

    def enqueue(self, data): 
        new_node = Node(data) 
        if self.rear: 
            self.rear.next = new_node 
            self.rear = new_node 
        else: 
            self.front = self.rear = new_node 

    def dequeue(self): 
        if self.front is None: 
            print("Queue is Empty") 
            return 
        temp = self.front 
        t = temp.data 
        self.front = self.front.next 
        if self.front is None:  # If the queue becomes empty
            self.rear = None
        print("Removed element is:", t) 

    def display(self): 
        if self.front is None: 
            print("Queue is Empty") 
            return 
        temp = self.front 
        print("Queue elements are: ")
        while temp: 
            print(temp.data, end=" ")
            temp = temp.next 
        print() 

s = Queue() 
print("1. Enqueue\n2. Dequeue\n3. Display\n4. Exit") 

while True: 
    i = int(input("Enter your choice: ")) 
    if i == 1: 
        ele = int(input("Enter an element: ")) 
        s.enqueue(ele) 
    elif i == 2: 
        s.dequeue() 
    elif i == 3: 
        s.display() 
    elif i == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
