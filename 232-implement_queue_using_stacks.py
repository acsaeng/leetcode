class MyQueue:
  def __init__(self):
    self.main = []
    self.spare = []
      
  def push(self, x: int) -> None:
    while self.main:
      self.spare.append(self.main.pop())

    self.main.append(x)

    while self.spare:
      self.main.append(self.spare.pop())

  def pop(self) -> int:
    return self.main.pop()

  def peek(self) -> int:
    return self.main[-1]

  def empty(self) -> bool:
    return not self.main


print('Case 1: ["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]')
myQueue = MyQueue()
print([None, myQueue.push(1), myQueue.push(2), myQueue.peek(), myQueue.pop(), myQueue.empty()])