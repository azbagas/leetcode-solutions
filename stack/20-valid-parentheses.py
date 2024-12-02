class Solution:
    def isValid(self, s: str) -> bool:
        # Initial stack
        stack = []

        # Define the brackets
        # Key: open bracket
        # Value: closing bracket
        brackets = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            # Check for the open bracket
            if c in brackets:
                stack.append(c)
            else:
                if len(stack) != 0 and c == brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("((){}"))