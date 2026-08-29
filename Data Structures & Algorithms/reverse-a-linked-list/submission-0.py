class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = head

        while current:
            next_node = current.next

            current.next = dummy.next
            dummy.next = current

            current = next_node

        return dummy.next