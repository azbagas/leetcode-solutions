from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # amount of rows and cols
        row_num = len(matrix)
        col_num = len(matrix[0])

        left = 0
        right = row_num * col_num - 1

        while left <= right:
            mid = (left + right) // 2
            mid_index = self.convertMainIndexToMatrixIndex(mid, col_num)

            if matrix[mid_index[0]][mid_index[1]] == target:
                return True

            if matrix[mid_index[0]][mid_index[1]] < target:
                # Move to the right
                left = mid + 1
            else:
                # Move to the left
                right = mid - 1

        return False

    def convertMainIndexToMatrixIndex(self, main_index: int, col_num: int) -> List[int]:
        return [main_index // col_num, main_index % col_num]


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
