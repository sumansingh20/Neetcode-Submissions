class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        suman = ListNode(0)
        temp = suman
        carry = 0
        while l1 or l2 or carry:
            x = 0
            y = 0
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next
            total = x + y + carry
            carry = total // 10
            temp.next = ListNode(total % 10)
            temp = temp.next
        return suman.next