from typing import List


class TimeMap:
    def __init__(self):
        self.dict = {}

        """
        Example:
        {
            'foo': [
                (1, 'bar'), 
                (4, 'bar2'), 
            ],
            'foo2': [
                (1, 'bar'), 
                (4, 'bar2'), 
            ],
        }
        """

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []

        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

        # do binary search
        arr = self.dict[key]
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]

            if arr[mid][0] < timestamp:
                # Move to the right
                left = mid + 1
            else:
                # Move to the left
                right = mid - 1

        # All timestamps are greater than given timestamp
        if right < 0:
            return ""

        return arr[right][1]


if __name__ == "__main__":
    # operations = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    # args = [
    #     [],
    #     ["foo", "bar", 1],
    #     ["foo", 1],
    #     ["foo", 3],
    #     ["foo", "bar2", 4],
    #     ["foo", 4],
    #     ["foo", 5],
    # ]

    operations = ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
    args = [
        [],
        ["love", "high", 10],
        ["love", "low", 20],
        ["love", 5],
        ["love", 10],
        ["love", 15],
        ["love", 20],
        ["love", 25],
    ]

    obj = None

    for i, operation in enumerate(operations):
        if operation == "TimeMap":
            obj = TimeMap()
            print("null")
        elif operation == "set":
            obj.set(args[i][0], args[i][1], args[i][2])
            print("null")
        elif operation == "get":
            res = obj.get(args[i][0], args[i][1])
            print(res)
        else:
            print("Invalid operation!")
            break
