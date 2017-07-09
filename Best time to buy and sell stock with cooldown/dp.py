class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell, rest = [0] * len(prices), [0] * len(prices), [0] * len(prices)
        for i in range(1, len(prices)):
            buy[i] = max(rest[i-1] - prices[i], buy[i-1])
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])
            rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
        return sell[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
