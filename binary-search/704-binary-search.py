from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        left = 0
        right = len(nums) - 1

        while left <= right:
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                # Move to the left
                right = mid - 1
            else:
                # Move to the right
                left = mid + 1

            mid = (left + right) // 2

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1, 0, 3, 5, 9, 12], 2))
