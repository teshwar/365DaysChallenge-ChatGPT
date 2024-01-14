"""
   Day 13: Data Structures (Stacks and Queues)
        Implement a stack and a queue.
        Solve a problem using these data structures.

"""

#Implement Class Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else: 
            return None
    def size(self):
        return len(self.items)

#Implement Class Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else: 
            raise IndexError("dequeue from an empty queue")
        
    def size(self):
        return len(self.item)
    
def problem_solver():
    #Example problem: Reverse a string using a stack
    input_string = "Bonjour !"

    #Use stack to reverse the string
    stack = Stack()
    for char in input_string:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    print(f"Original String: {input_string}")
    print(f"Reversed String: {reversed_string}")

if __name__ == "__main__":
    problem_solver()