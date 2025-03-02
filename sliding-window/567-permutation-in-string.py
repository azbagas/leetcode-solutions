from typing import List


# 2 hours taken to solve this problem 🗿
# I think it can be refactored for a better looks

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count = dict()

        # Count all char in s1
        for char in s1:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

        checks = dict()

        left, right = 0, 0
        while right < len(s2):
            if s2[right] in char_count:
                if s2[right] not in checks:
                    checks[s2[right]] = 1
                else:
                    if checks[s2[right]] >= char_count[s2[right]]:
                        if char_count == checks:
                            return True

                        while checks[s2[right]] >= char_count[s2[right]]:
                            checks[s2[left]] -= 1
                            left += 1

                    checks[s2[right]] += 1

                right += 1
            else:
                if char_count == checks:
                    return True

                checks = dict()
                right += 1
                left = right

        if char_count == checks:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion("ab", "eidbaooo"))
    print(solution.checkInclusion("ab", "eidboaoo"))
    print(solution.checkInclusion("adc", "dcda"))
    print(solution.checkInclusion("abc", "cccccbabbbaaaa"))
    print(solution.checkInclusion("mart", "karma"))
    print(solution.checkInclusion("dinitrophenylhydrazine", "acetylphenylhydrazine"))
