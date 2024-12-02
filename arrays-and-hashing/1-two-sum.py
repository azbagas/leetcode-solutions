from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            # Pengecekan "complement in hashmap" ini memakan kompleksitas yang konstan
            # Sama halnya dengan mengakses element array pakai index
            # Jadi tidak sequential
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                # Key -> bilangannya
                # Value -> indexnya
                hashmap[nums[i]] = i
        return []
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([-3,4,3,90], 0))