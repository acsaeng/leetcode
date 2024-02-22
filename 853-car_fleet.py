class Solution:
  def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
    pos_speed = [[p, s] for p, s in zip(position, speed)]
    slowest_time = 0
    num_fleets = 0

    for pos, speed in sorted(pos_speed, reverse=True):
      time = (target - pos) / speed

      if not slowest_time or time > slowest_time:
        num_fleets += 1
        slowest_time = time
      
    return num_fleets


print('\nCase 1: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]')
print('Answer:', Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))

print('\nCase 2: target = 10, position = [3], speed = [3]')
print('Answer:', Solution().carFleet(10, [3], [3]))

print('\nCase 3: target = 100, position = [0, 2, 4], speed = [4, 2, 1]')
print('Answer:', Solution().carFleet(100, [0, 2, 4], [4, 2, 1]))