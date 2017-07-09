def maxProfit(prices):
    import sys
    min_price = sys.maxsize  # 9223372036854775807
    max_profit = 0
    for i in prices:
        min_price = min(min_price, i)
        max_profit = max(max_profit, i - min_price)
    return max_profit

assert maxProfit([7, 6, 4, 3, 1]) == 0
assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
