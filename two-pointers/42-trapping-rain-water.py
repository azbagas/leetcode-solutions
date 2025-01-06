from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = height[0]
        max_right = height[len(height) - 1]
        water = 0

        while left < right:
            # Maintain the max height of left and right 
            if max_left > max_right:
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]
            else:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]

        return water

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = max_right = 0
        water = 0

        while left < right:
            if height[left] > height[right]:
                # Fill the shorter with water (height right)
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1
            else:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1

        return water
"""

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        # Search for max height index
        max_height_idx = 0
        for i in range(1, len(height)):
            if height[max_height_idx] < height[i]:
                max_height_idx = i

        water = 0

        # Do for loop to the left side of max height
        max_height_left = 0
        for i in range(max_height_idx - 1, 0, -1):
            if height[i] >=  max_height_left:
                max_height_left = max(height[0:i])
                if max_height_left < height[i]:
                    continue

            current_water = max_height_left - height[i]
            water += current_water

        # Do for loop to the right side of max height
        max_height_right = 0
        for i in range(max_height_idx + 1, len(height) - 1):
            if height[i] >= max_height_right:
                max_height_right = max(height[i + 1 :])
                if max_height_right < height[i]:
                    continue

            current_water = max_height_right - height[i]
            water += current_water

        return water
"""

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        # Search for max height index
        max_height_idx = 0
        for i in range(1, len(height)):
            if height[max_height_idx] < height[i]:
                max_height_idx = i

        water = 0

        # Do for loop to the left side of max height
        for i in range(max_height_idx - 1, 0, -1):
            max_height_left = max(height[0:i])

            if max_height_left == 0 or max_height_left < height[i]:
                continue

            current_water = max_height_left - height[i]
            water += current_water

        # Do for loop to the right side of max height
        for i in range(max_height_idx + 1, len(height) - 1):
            max_height_right = max(height[i + 1 :])

            if max_height_right == 0 or max_height_right < height[i]:
                continue

            current_water = max_height_right - height[i]
            water += current_water

        return water
"""

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
