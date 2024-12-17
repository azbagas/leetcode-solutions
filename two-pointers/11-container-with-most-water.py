from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height) - 1

        water = 0
        while left_idx < right_idx:
            current_water = min(height[left_idx], height[right_idx]) * (right_idx - left_idx)
            
            if current_water > water:
                water = current_water

            # Change index
            if height[left_idx] < height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1

        return water


"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height) - 1

        water = 0
        while left_idx < right_idx:
            smallest_height, smallest_index = -1, -1

            if height[left_idx] >= height[right_idx]:
                smallest_height = height[right_idx]
                smallest_index = right_idx
            else:
                smallest_height = height[left_idx]
                smallest_index = left_idx

            current_water = smallest_height * (right_idx - left_idx)
            if current_water > water:
                water = current_water

            # Change index
            if smallest_index == left_idx:
                left_idx += 1
            else:
                right_idx -= 1

        return water
"""


if __name__ == "__main__":
    solution = Solution()
    # print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
    # print(solution.maxArea([1,1]))
    print(solution.maxArea([1, 2, 4, 3]))
