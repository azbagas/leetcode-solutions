from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack: List[str] = []

        for token in tokens:
            # If token is a number
            if token not in operators:
                stack.append(token)
                continue
            
            # If token is an operator, calculate it
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            result = None

            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            else:
                result = num1 / num2
            
            stack.append(result)
        
        return int(stack.pop())

if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(["4","13","5","/","+"]))