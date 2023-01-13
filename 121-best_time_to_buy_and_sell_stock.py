class Solution:
  def max_profit(self, prices: list[int]) -> int:
    current_max_profit = 0
    for day, price in enumerate(prices):
      if price > current_max_profit:
        fwd_day_prices = prices[day + 1:]

        if len(fwd_day_prices):
          max_day_profit = max(fwd_day_prices) - price

          if max_day_profit > current_max_profit:
            current_max_profit = max_day_profit

    return current_max_profit



if __name__ == '__main__':
  solution = Solution()

  print('Case 1: prices = [7  1, 5, 3, 6, 4]')
  print('Answer:', solution.max_profit([7, 1, 5, 3, 6, 4]))

  print('\nCase 2: prices = [7, 6, 4, 3, 1]')
  print('Answer:', solution.max_profit([7, 6, 4, 3, 1]))