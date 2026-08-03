# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # Find middle of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half of list
        prev, curr = None, slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Interweave the two lists (first half and second half)
        first, second = head, prev
        while second.next:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2