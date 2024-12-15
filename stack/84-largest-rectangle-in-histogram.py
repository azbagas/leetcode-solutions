from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Example:
        heights                  = [2, 1, 2]
        left_higher_or_same_idx  = [-1, -1, 1]
        right_higher_or_same_idx = [1, 3, 3]

        area                     = [2, 3, 2]
        """

        heights_len = len(heights)

        left_higher_or_same_idx = [-1] * heights_len
        right_higher_or_same_idx = [-1] * heights_len

        # Calculate left_higher_or_same_idx for each height
        for i in range(heights_len):
            if i == 0:
                # First height will be its index
                left_higher_or_same_idx[i] = i - 1
                continue

            left_idx = i - 1
            while left_idx >= 0 and heights[left_idx] >= heights[i]:
                left_idx = left_higher_or_same_idx[left_idx]
            left_higher_or_same_idx[i] = left_idx

        # Calculate right_higher_or_same_idx for each height
        for i in range(heights_len - 1, -1, -1):
            if i == heights_len - 1:
                # Last height will be its index
                right_higher_or_same_idx[i] = i + 1
                continue

            right_idx = i + 1
            while right_idx < heights_len and heights[right_idx] >= heights[i]:
                right_idx = right_higher_or_same_idx[right_idx]
            right_higher_or_same_idx[i] = right_idx

        # Calculate area
        area = [0] * heights_len
        for i in range(heights_len):
            area[i] = heights[i] * (
                (right_higher_or_same_idx[i] - 1) - (left_higher_or_same_idx[i] + 1) + 1
            )

        return max(area)


"""
# Time Limit
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        largest_area = 0

        for i in range(len(heights)):
            length = 1
            current_height = heights[i]
            area = length * current_height

            for j in range(len(heights) - i - 1):
                next_height = heights[i + j + 1]
                if next_height < current_height:
                    current_height = next_height

                length += 1
                new_area = current_height * length

                if new_area > area:
                    area = new_area

            if area > largest_area:
                largest_area = area

        return largest_area
"""


if __name__ == "__main__":
    solution = Solution()
    # print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    # print(solution.largestRectangleArea([4,2,0,3,2,4,3,4]))
    # print(solution.largestRectangleArea([5,4,1,2]))
    print(solution.largestRectangleArea([2, 1, 2]))
