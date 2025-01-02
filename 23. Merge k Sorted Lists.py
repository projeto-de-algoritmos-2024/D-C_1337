from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def divide_and_conquer(left: int, right: int) -> Optional[ListNode]:
            if left == right:
                return lists[left]
            if left > right:
                return None

            mid = left + (right - left) // 2
            left_merged = divide_and_conquer(left, mid)
            right_merged = divide_and_conquer(mid + 1, right)

            return merge_two_lists(left_merged, right_merged)

        def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next

            current.next = list1 if list1 else list2

            return dummy.next

        if not lists:
            return None

        return divide_and_conquer(0, len(lists) - 1)