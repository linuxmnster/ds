class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class Stack: 
    def __init__(self): 
        self.top = None 

    def push(self, data): 
        new_node = Node(data) 
        if self.top: 
            new_node.next = self.top 
        self.top = new_node 

    def pop(self): 
        if self.top is None: 
            print("Stack is Empty") 
            return 
        temp = self.top 
        t = temp.data 
        self.top = temp.next 
        print("Removed element is:", t) 

    def display(self): 
        if self.top is None: 
            print("Stack is Empty") 
            return 
        temp = self.top 
        while temp: 
            print(temp.data) 
            temp = temp.next 

s = Stack() 
print("1. PUSH\n2. POP\n3. DISPLAY\n4. EXIT") 

while True: 
    i = int(input("Enter your choice: ")) 
    if i == 1: 
        ele = int(input("Enter an element: ")) 
        s.push(ele) 
    elif i == 2: 
        s.pop() 
    elif i == 3: 
        s.display() 
    elif i == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
