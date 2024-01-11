class MyQueue:
  def __init__(self):
    self.in_stack = []
    self.out_stack = []
      
  def push(self, x: int) -> None:
    self.in_stack.append(x)

  def pop(self) -> int:
    self.peek()
    return self.out_stack.pop()

  def peek(self) -> int:
    if not self.out_stack:
      while self.in_stack:
        self.out_stack.append(self.in_stack.pop())
    
    return self.out_stack[-1]

  def empty(self) -> bool:
    return not self.in_stack and not self.out_stack


print('Case 1: ["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]')
myQueue = MyQueue()
print([None, myQueue.push(1), myQueue.push(2), myQueue.peek(), myQueue.pop(), myQueue.empty()])