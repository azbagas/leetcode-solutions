from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack stores the index
        # So, we can calculate the range to the next greater temperature of the current index
        stack = []
        # Initialize answer with all 0
        answer = [0 for _ in range(len(temperatures))]

        for i, temperature in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(i)
                continue
            
            while(True):
                if len(stack) == 0:
                    stack.append(i)
                    break
                
                # Compare current temperature to the top of the stack
                if temperature > temperatures[stack[-1]]:
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    stack.append(i)
                    break

        return answer
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))