from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 'second' is the head of the second half
        second = slow.next
        # Cut the list
        slow.next = None

        # 2. Reverse the second half
        new_head = None
        while second:
            temp = second.next
            second.next = new_head
            new_head = second
            second = temp
        # Make 'second' head of the second half again
        second = new_head

        # 3. Merge the two halves
        # Note: If the list was [1,2,3,4], first is [1,2] and second is [4]
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        ## First attempt
        # if head.next == None:
        #     return

        # stack = []
        # temp = head.next
        # while temp != None:
        #     stack.append(temp)
        #     temp = temp.next

        # temp = head
        # while len(stack) != 0:
        #     temp.next = stack.pop()
        #     temp = temp.next

        #     if len(stack) == 0:
        #         break

        #     temp.next = stack.pop(0)
        #     temp = temp.next

        # temp.next = None


if __name__ == "__main__":

    data = [1, 2, 3, 4, 5]
    linked_list = LinkedList()
    for val in data:
        linked_list.insertLast(val)

    solution = Solution()
    solution.reorderList(linked_list.head)

    print(linked_list.getList())
