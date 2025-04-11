from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            # Remove the element going out of the window
            # (i - k) is left pointer
            if i >= k and nums[i - k] == q[0]:
                q.popleft()

            # Remove all smaller elements from the back (they won't be max)
            while q and q[-1] < nums[i]:
                q.pop()

            q.append(nums[i])

            # Append the max once the window is full
            if i >= k - 1:
                result.append(q[0])

        return result


""" 
# First form
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Using double ended queue
        q = deque()

        max_sliding_window = []

        # Initialize first window
        for i in range(k):
            # If queue empty
            if len(q) == 0:
                q.append(nums[i])
                continue

            # Pop right element if it's smaller than current
            while len(q) != 0 and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        # Append the peak (peak is a max within the window)
        max_sliding_window.append(q[0])

        left = 1

        for right in range(k, len(nums)):
            # Remove the left most window's element
            if nums[left - 1] == q[0]:
                q.popleft()

            # Add the right new element
            while len(q) != 0 and q[-1] < nums[right]:
                q.pop()
            q.append(nums[right])

            max_sliding_window.append(q[0])

            left += 1

        return max_sliding_window
"""

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
