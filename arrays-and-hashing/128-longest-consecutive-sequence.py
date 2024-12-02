from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Change list into set
        nums_set = set(nums)

        # Check
        longest = 0
        for num in nums_set:
            # Check only for base num
            if num - 1 not in nums_set:
                current_longest = 1
                i = 1
                while(True):
                    if num+i in nums_set:
                        current_longest += 1
                        i += 1
                    else:
                        break
            
                if current_longest > longest:
                    longest = current_longest
        
        return longest
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))