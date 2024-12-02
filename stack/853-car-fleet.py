from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars based on position
        combined = sorted(zip(position, speed), key=lambda x: x[0])
        position, speed = zip(*combined)

        # Calculate the time to finished each car
        time_to_finished: List[float] = []

        for i in range(len(position)):
            time_to_finished.append((target - position[i]) / speed[i])

        # Do monotonic stack
        stack: List[float] = []

        for i, time in enumerate(time_to_finished):
            if len(stack) == 0:
                stack.append(time)
                continue

            while True:
                if time >= stack[-1]:
                    stack.pop()
                else:
                    stack.append(time)
                    break

                if len(stack) == 0:
                    stack.append(time)
                    break

        return len(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
