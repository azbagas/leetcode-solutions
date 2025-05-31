from typing import Optional


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


class Solution:
    # Iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_head = None

        while curr != None:
            temp = curr.next
            curr.next = new_head

            new_head = curr
            curr = temp

        return new_head

    # Recursive
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head == None:
    #         return None

    #     new_head = head
    #     if head.next:
    #         new_head = self.reverseList(head.next)
    #         head.next.next = head
    #     head.next = None

    #     return new_head


if __name__ == "__main__":
    solution = Solution()

    values = [1, 2, 3, 4, 5]

    linked_list = LinkedList()
    for value in values:
        linked_list.insertLast(value)

    print(linked_list.getList())
    linked_list.head = solution.reverseList(linked_list.head)
    print(linked_list.getList())
