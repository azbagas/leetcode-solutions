from typing import List

class Solution:
    # 3rd solution
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_set = set()
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    digit = board[i][j]
                    if (i, digit) in board_set or (digit, j) in board_set or (i//3, j//3, digit) in board_set:
                        return False
                    board_set.add((i, digit))
                    board_set.add((digit, j))
                    board_set.add((i//3, j//3, digit))
        
        return True
        
        # Contoh
        # (i, digit): (0, '3') baris 0 memiliki elemen '3'
        # (digit, j): ('0', 3) kolom 3 memiliki elemen '0'
        # we are not the same because the element is string

        # Jadi, kunci set-nya merupakan tuple
    
    # # 2nd solution
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     # Check rows
    #     for row in board:
    #         digit_row = [digit for digit in row if digit != "."]
    #         if self.containsDuplicate(digit_row):
    #             return False

    #     # Check columns
    #     for col in list(zip(*board)):
    #         digit_col = [digit for digit in col if digit != "."]
    #         if self.containsDuplicate(digit_col):
    #             return False

    #     # Check 3x3 subgrids
    #     # i: row
    #     for i in range(0, 7, 3):
    #         # j: column
    #         for j in range(0, 7, 3):
    #             subgrid = [row[j:j+3] for row in board[i:i+3]]
    #             flattened = [digit for row in subgrid for digit in row if digit != "."]
    #             if self.containsDuplicate(flattened):
    #                 return False
        
    #     return True
    
    # # 1st solution
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     # Check row
    #     for row in board:
    #         digit_row = [digit for digit in row if digit != "."]
    #         if self.containsDuplicate(digit_row):
    #             return False

    #     # Check column
    #     for col_index in range(len(board[0])):
    #         digit_col = [row[col_index] for row in board if row[col_index] != "."]
    #         if self.containsDuplicate(digit_col):
    #             return False

    #     # Check 3x3 subgrid
    #     start_row, end_row = 0, 3
    #     start_col, end_col = 0, 3

    #     for i in range(3):
    #         for j in range(3):
    #             subgrid = [row[start_col:end_col] for row in board[start_row:end_row]]
    #             flattened = [digit for row in subgrid for digit in row if digit != "."]
    #             if self.containsDuplicate(flattened):
    #                 return False
    #             start_col += 3
    #             end_col += 3
    #         start_col, end_col = 0, 3
    #         start_row += 3
    #         end_row += 3
        
    #     return True

    # def containsDuplicate(self, elements: List[int]) -> bool:
    #     temp_set = set()
    #     for element in elements:
    #         temp_set.add(element)
        
    #     if len(elements) == len(temp_set):
    #         return False
    #     else:
    #         return True

if __name__ == "__main__":
    solution = Solution()
    print(
        solution.isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )
