class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        suman = None
        temp = head
        while temp:
            nxt = temp.next
            temp.next = suman
            suman = temp
            temp = nxt
        return suman