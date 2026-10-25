class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        curr = slow
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        first = head
        second = prev
        while second != None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True