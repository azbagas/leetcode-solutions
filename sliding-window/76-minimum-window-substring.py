from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Initialize hash map
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        s_count = {}
        left = 0
        matches = 0
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            if s[right] in t_count:
                s_count[s[right]] = s_count.get(s[right], 0) + 1
                if s_count[s[right]] == t_count[s[right]]:
                    matches += 1  # A character has reached its required frequency

            while matches == len(t_count):  # Valid window found
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    min_start = left

                # Try to shrink the window
                if s[left] in t_count:
                    s_count[s[left]] -= 1
                    if (
                        s_count[s[left]] < t_count[s[left]]
                    ):  # Character no longer satisfies the condition
                        matches -= 1

                left += 1  # Move the left pointer

        return s[min_start : min_start + min_len] if min_len != float("inf") else ""


if __name__ == "__main__":
    solution = Solution()
    # print(solution.minWindow("FADOBECODEBANC", "ABC"))
    # print(solution.minWindow("a", "a"))
    # print(solution.minWindow("bba", "ab"))
    # print(solution.minWindow("bba", "ab"))
    # print(solution.minWindow("a", "b"))
    # print(solution.minWindow("ab", "a"))
    # print(solution.minWindow("bbaac", "aba"))
    print(solution.minWindow("aaflslflsldkalskaaa", "aaa"))
