from typing import List, Dict


class Solution:
    # Two pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right_index = len(numbers) - 1
        left_index = 0

        while left_index < right_index:
            sum = numbers[left_index] + numbers[right_index]
            if sum == target:
                return [left_index + 1, right_index + 1]
            elif sum > target:
                # Decrease the right index
                right_index -= 1
            else:
                # Increase the left index
                left_index += 1


"""
# Dictionary
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Create dict
        num_dict: Dict[int, List[int]] = {}

        for i in range(len(numbers)):
            if numbers[i] in num_dict:
                num_dict[numbers[i]].append(i)
            else:
                num_dict[numbers[i]] = [i]

        # Search for the numbers
        index1 = -1
        index2 = -1
        for num in num_dict:
            diff = target - num
            if diff in num_dict:
                index1 = num_dict[num].pop() + 1
                index2 = num_dict[diff].pop() + 1
                break

        if index1 > index2:
            index1, index2 = index2, index1

        return [index1, index2]
"""

if __name__ == "__main__":
    solution = Solution()
    # print(solution.twoSum([2, 7, 11, 15], 9))
    # print(solution.twoSum([-1, 0], -3))
    print(solution.twoSum([0, 0, 3, 4], 0))
