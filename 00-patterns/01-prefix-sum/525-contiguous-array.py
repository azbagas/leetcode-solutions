from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        max_length = 0
        prefix_sum = {0: -1}

        for i, num in enumerate(nums):
            if num == 0:
                sum -= 1
            else:
                sum += 1

            if sum in prefix_sum:
                max_length = max(max_length, i - prefix_sum[sum])
            else:
                prefix_sum[sum] = i

        return max_length

    # Brute Force
    # def findMaxLength(self, nums: List[int]) -> int:
    #     max_length = 0
    #     n = len(nums)

    #     for i in range(n):
    #         zero_count = 0
    #         one_count = 0

    #         for j in range(i, n):
    #             if nums[j] == 0:
    #                 zero_count += 1
    #             else:
    #                 one_count += 1

    #             if zero_count == one_count:
    #                 max_length = max(max_length, j - i + 1)

    #     return max_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]))
