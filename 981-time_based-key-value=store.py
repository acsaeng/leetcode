class TimeMap:
  def __init__(self):
    self.store = {}
      
  def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self.store:
      self.store[key] = []

    self.store[key].append([value, timestamp])

  def get(self, key: str, timestamp: int) -> str:
    most_recent_value = ''
    values = self.store.get(key, [])
    left, right = 0, len(values) - 1

    while left <= right:
      middle = left + ((right - left) // 2)
      
      if values[middle][1] <= timestamp:
        most_recent_value = values[middle][0]
        left = middle + 1
      elif values[middle][1] > timestamp:
        right = middle - 1
    
    return most_recent_value


print('Case 1: ["TimeMap", "set", "get", "get", "set", "get", "get"], [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]')
obj = TimeMap()
print('Answer:', [None, obj.set('foo', 'bar', 1), obj.get('foo', 1), obj.get('foo', 3), obj.set('foo', 'bar2', 4), obj.get('foo', 4), obj.get('foo', 5)])