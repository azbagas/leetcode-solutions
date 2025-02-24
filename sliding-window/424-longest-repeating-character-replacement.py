from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars_count = dict()
        left = 0
        substring_length = 0
        max_count = 0

        for right, char in enumerate(s):
            if char not in chars_count:
                chars_count[char] = 1
            else:
                chars_count[char] += 1

            max_count = max(list(chars_count.values()))

            substring_length = right - left + 1
            if substring_length - max_count > k:
                chars_count[s[left]] -= 1
                left += 1
                substring_length -= 1

        return substring_length


if __name__ == "__main__":
    solution = Solution()
    # print(solution.characterReplacement("ABAB", 2))
    # print(solution.characterReplacement("AABABBA", 1))
    print(solution.characterReplacement("AABA", 0))
