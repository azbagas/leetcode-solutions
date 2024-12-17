from typing import List, Dict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if nums[0] > 0:
            return []

        triplets = []

        for i in range(len(nums)):
            left_idx = i + 1
            right_idx = len(nums) - 1

            # Avoid duplicate
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            while left_idx < right_idx:
                sum = nums[i] + nums[left_idx] + nums[right_idx]
                if sum > 0:
                    right_idx -= 1
                elif sum < 0:
                    left_idx += 1
                else:
                    triplets.append([nums[i], nums[left_idx], nums[right_idx]])
                    left_idx += 1
                    # Avoid duplicate
                    while nums[left_idx] == nums[left_idx - 1] and left_idx < right_idx:
                        left_idx += 1

        return triplets


"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if nums[0] > 0:
            return []

        # Turn into dict
        nums_dict: Dict[int, List] = {}
        for i, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = [i]
            else:
                nums_dict[num].append(i)

        # Search for triplets
        triplets = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                two_sum_neg = (nums[i] + nums[j]) * -1
                if two_sum_neg in nums_dict and nums_dict[two_sum_neg][-1] > j:
                    triplets.append([nums[i], nums[j], two_sum_neg])

        return triplets
"""

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(solution.threeSum([3, 0, -2, -1, 1, 2]))
    # print(solution.threeSum([0, 0, 0]))
