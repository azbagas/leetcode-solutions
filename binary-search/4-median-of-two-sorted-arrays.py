from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure nums2 is always has more num than nums1
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l1, r1 = 0, len(nums1) - 1

        while True:
            m1 = (l1 + r1) // 2
            m2 = half - m1 - 2

            nums1_mid = nums1[m1] if m1 >= 0 else float("-inf")
            nums1_mid_right = nums1[m1 + 1] if m1 + 1 < len(nums1) else float("inf")
            nums2_mid = nums2[m2] if m2 >= 0 else float("-inf")
            nums2_mid_right = nums2[m2 + 1] if m2 + 1 < len(nums2) else float("inf")

            if nums1_mid <= nums2_mid_right and nums2_mid <= nums1_mid_right:
                if total % 2 != 0:
                    # odd
                    return min(nums1_mid_right, nums2_mid_right)
                else:
                    # even
                    return (
                        max(nums1_mid, nums2_mid)
                        + min(nums1_mid_right, nums2_mid_right)
                    ) / 2
            elif nums1_mid > nums2_mid_right:
                r1 = m1 - 1
            else:
                l1 = m1 + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
