class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        values.reverse()

        new_head = ListNode(values[0])
        current = new_head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next

        return new_head