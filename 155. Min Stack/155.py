

class MinStackWith2Stack():
    '''
    Use extra stack to track of the current minimum value
    O(n) runtime
    O(n) space for extra stack
    '''
    def __init__():
        self.primary_stack = []
        self.minimum_stack = []
    
    def top():
        if len(self.primary_stack) == 0:
            return None
        else:
            return self.primary_stack[-1]

    def push(x):
        self.primary_stack.append(x)
        try:
            min_value = x if self.minimum_stack[-1] > x else self.minimum_stack[-1]
            self.minimum_stack.append(min_value)
        except IndexError:
            self.minimum_stack.append(x)
        # if len(self.minimum_stack) != 0:
        #     min_value = x if self.minimum_stack[-1] > x else self.minimum_stack[-1]
        #     self.minimum_stack.append(min_value)
        # else:
        #     self.minimum_stack.append(x)
    
    def pop():
        self.primary_stack.pop()
        self.minimum_stack.pop()
    
    def get_min():
        if len(self.minimum_stack) == 0:
            return None
        else:
            return self.minimum_stack[-1]
    

class MinStackWith2StackOptimal():
    def __init__():
        self.primary_stack = []
        self.minimum_stack = []

    def push(x):
        self.primary_stack.append(x)
        try:
            if self.minimum_stack[-1] >= x:
                self.minimum_stack.append(x)
        except IndexError:
            self.minimum_stack.append(x)

    def pop():
        if len(self.minimum_stack) != 0 and len(self.primary_stack) != 0 and self.minimum_stack[-1] == self.primary_stack[-1]:
            self.minimum_stack.pop()
        if len(self.primary_stack) != 0:
            self.primary_stack.pop()

    def get_min():
        if len(self.minimum_stack) == 0:
            return None
        else:
            return self.minimum_stack[-1]
