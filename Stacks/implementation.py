class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.isEmpty():
            print('Cannot pop; Stack underflow')
        else:
            print(f'Popped: {self.stack.pop()}')
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            print(f'Peek: {self.stack[-1]}')
            
    def display(self):
        print('Stack:')
        if self.isEmpty():
            print('Empty')
        else:
            for i in self.stack[::-1]:
                print(i)
