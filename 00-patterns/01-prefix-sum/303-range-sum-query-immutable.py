from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        # Calculate prefix sum
        self.prefix_sum = []
        curr = 0
        for num in self.nums:
            curr += num
            self.prefix_sum.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]

        return self.prefix_sum[right] - self.prefix_sum[left - 1]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sumRange(0, 2))
    print(obj.sumRange(2, 5))
    print(obj.sumRange(0, 5))
