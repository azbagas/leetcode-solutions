from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertLast(self, val):
        if self.head == None:
            new_node = ListNode(val)
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = ListNode(val)

    def getList(self) -> list:
        values = []
        temp = self.head
        while temp != None:
            values.append(temp.val)
            temp = temp.next

        return values

    def getTail(self) -> ListNode:
        temp = self.head
        while temp.next != None:
            temp = temp.next

        return temp


class Solution:
    # Hash
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     hash_table = set()
    #     temp = head
    #     while temp != None:
    #         if temp in hash_table:
    #             return True
    #         else:
    #             hash_table.add(temp)
    #             temp = temp.next
    #     return False

    # Fast and Slow
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Slow: 1 step
        # Fast: 2 steps
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    # Test data cycle LinkedList
    data1 = [3, 2, 0, -4]
    linked_list1 = LinkedList()
    for val in data1:
        linked_list1.insertLast(val)
    node2 = linked_list1.head.next
    tail = linked_list1.getTail()
    tail.next = node2

    solution = Solution()
    print(solution.hasCycle(linked_list1.head))
