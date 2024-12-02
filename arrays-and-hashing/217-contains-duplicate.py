from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp_set = set()
        for num in nums:
            temp_set.add(num)
        
        if len(nums) == len(temp_set):
            return False
        else:
            return True
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1,2,3,4,5]))