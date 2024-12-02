from typing import List

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		if len(nums1) == 0 and len(nums2) != 0:
			return self.findMedianOfList(nums2)

		if len(nums2) == 0 and len(nums1) != 0:
			return self.findMedianOfList(nums1)

		if len(nums1) == 0 and len(nums2) == 0:
			return 0

		i = 0
		j = 0
		result = []

		while(i != len(nums1) or j != len(nums2)):
			if i == len(nums1):
				result.extend(nums2[j:])
				break

			if j == len(nums2):
				result.extend(nums1[i:])
				break

			if nums1[i] < nums2[j]:
				result.append(nums1[i])
				i += 1
			else:
				result.append(nums2[j])
				j += 1

		print(result)

		return self.findMedianOfList(result)

	def findMedianOfList(self, nums: List[int]) -> float:
		if len(nums) % 2 != 0:
			return nums[(int)(len(nums) / 2)]
		else:
			return (nums[(int)(len(nums) / 2)] + nums[(int)((len(nums) / 2) - 1)]) / 2

if __name__ == "__main__":
	solution = Solution()
	print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))