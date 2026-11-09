class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next
        nxt = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = nxt
            nxt = cur
            cur = temp
        prev.next.next = cur
        prev.next = nxt
        return dummy.next