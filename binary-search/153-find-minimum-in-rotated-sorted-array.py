from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Move to the right
                left = mid + 1
            else:
                # Move to the left
                right = mid - 1

            if nums[mid] < result:
                result = nums[mid]

        return result


if __name__ == "__main__":
    solution = Solution()
    # print(solution.findMin([5, 1, 2, 3, 4]))
    # print(solution.findMin([1, 2, 3, 4, 5]))
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))
