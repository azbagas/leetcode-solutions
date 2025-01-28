from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left part is sorted
            if nums[left] <= nums[mid]:
                if target <= nums[mid] and nums[left] <= target:
                    # Move to the left
                    right = mid - 1
                else:
                    # Move to the right
                    left = mid + 1
            # Right part is sorted
            else:
                if target >= nums[mid] and nums[right] >= target:
                    # Move to the right
                    left = mid + 1
                else:
                    # Move to the left
                    right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(solution.search([3, 5, 1], 3))
    print(solution.search([3, 1], 1))
    print(solution.search([1, 3], 1))
    print(solution.search([5, 1, 3], 5))
    print(solution.search([4, 5, 6, 7, 8, 1, 2, 3], 8))
