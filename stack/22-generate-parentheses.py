from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []

        # open: remaining of open brackets
        # close: remaning of close brackets
        def recursive(open: int, close: int, parenthesis: str) -> None:
            if open == 0 and close == 0:
                combinations.append(parenthesis)
                return

            if open > 0:
                recursive(open - 1, close, parenthesis + "(")
            
            if close > open:
                recursive(open, close - 1, parenthesis + ")")

        recursive(open=n, close=n, parenthesis="")
        return combinations
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))