from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / mid)

            if total_hours <= h:
                # Check if there is smaller speeds
                result = mid
                right = mid - 1
            else:
                # Try faster speeds
                left = mid + 1

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))
