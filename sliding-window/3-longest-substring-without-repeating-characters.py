from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = set()

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            longest = max(longest, i - left + 1)

        return longest


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    # print(solution.lengthOfLongestSubstring("abcbbcbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
