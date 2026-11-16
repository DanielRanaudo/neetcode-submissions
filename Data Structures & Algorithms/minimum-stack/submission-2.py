class MinStack:

    def __init__(self):
        self.stack = [] 
        self.min_track = []
        self.minim = float('inf')


    def push(self, val: int) -> None:
        self.stack.append(val)

        self.minim = min(val, self.minim)
        self.min_track.append(self.minim)

    def pop(self) -> None:
        self.stack.pop()

        old_min = self.min_track.pop()
        if self.min_track: 
            self.minim = self.min_track[-1]
        else: 
            self.minim = float('inf')

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_track[-1]
        
