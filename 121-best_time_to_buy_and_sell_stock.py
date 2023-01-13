class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
      if price < min_price:
        min_price = price
      elif price - min_price > max_profit:
        max_profit = price - min_price 

    return max_profit


if __name__ == '__main__':
  solution = Solution()

  print('Case 1: prices = [7  1, 5, 3, 6, 4]')
  print('Answer:', solution.maxProfit([7, 1, 5, 3, 6, 4]))

  print('\nCase 2: prices = [7, 6, 4, 3, 1]')
  print('Answer:', solution.maxProfit([7, 6, 4, 3, 1]))