class MinStack:
  def __init__(self):
    self.stack = []
    self.min_stack = []
      
  def push(self, val: int) -> None:
    self.stack.append(val)
    self.min_stack.append(val if not self.min_stack or val < self.getMin() else self.getMin())

  def pop(self) -> None:
    self.stack.pop()
    self.min_stack.pop()
      
  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.min_stack[-1]


print('Case 1: ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], [[], [-2], [0], [-3], [], [], [], []]')
minStack = MinStack()
print([None, minStack.push(-2), minStack.push(0), minStack.push(-3), minStack.getMin(), minStack.pop(), minStack.top(), minStack.getMin()])