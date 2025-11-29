from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getList(head: ListNode):
    values = []
    temp = list
    while temp != None:
        values.append(temp.val)
        temp = temp.next

    return values

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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        resultHead = ListNode()
        resultCurr = resultHead

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                resultCurr.next = ListNode(list1.val)
                list1 = list1.next
            else: 
                resultCurr.next = ListNode(list2.val)
                list2 = list2.next
            resultCurr = resultCurr.next
        
        # Let the rest is list2
        if list1 == None:
            resultCurr.next = list2

        # Let the rest is list1
        if list2 == None:
            resultCurr.next = list1
        
        return resultHead.next


if __name__ == "__main__":
    values1 = [1, 2, 4]
    values2 = [1, 3, 4]

    list1 = LinkedList()
    for value in values1:
        list1.insertLast(value)

    list2 = LinkedList()
    for value in values2:
        list2.insertLast(value)

    result = LinkedList()

    solution = Solution()
    result.head = solution.mergeTwoLists(list1.head, list2.head)
    print(result.getList())
