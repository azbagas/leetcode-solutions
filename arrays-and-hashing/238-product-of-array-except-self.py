from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        
        # Inisialisasi array answer dengan setiap element 1
        answer = [1] * nums_length

        # Setiap nilai answer kita buat menjadi prefix pada index ke-i
        prefix = 1
        for i in range(0, nums_length):
            answer[i] = answer[i] * prefix
            prefix *= nums[i]
        
        # Kalikan dengan suffix-nya
        suffix = 1
        for i in range(nums_length-1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix *= nums[i]

        return answer
    
    # Solusi 1
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     prefix = [1] * len(nums)
    #     suffix = [1] * len(nums)

    #     for i in range(1, len(nums)):
    #         prefix[i] = prefix[i-1] * nums[i-1]
        
    #     for i in range(len(nums)-2, -1, -1):
    #         suffix[i] = suffix[i+1] * nums[i+1]

    #     answer = []
    #     for i in range(len(nums)):
    #         answer.append(prefix[i] * suffix[i])
        
    #     return answer

if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))