from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_small = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < current_small:
                current_small = prices[i]
            else:
                current_profit = prices[i] - current_small
                if current_profit > profit:
                    profit = current_profit

        return profit


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
