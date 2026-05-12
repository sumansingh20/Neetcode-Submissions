class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        suman = []
        temp = head
        while temp:
            suman.append(temp.val)
            temp = temp.next
        for i in range(0, len(suman), k):
            if i + k <= len(suman):
                left = i
                right = i + k - 1
                while left < right:
                    suman[left], suman[right] = suman[right], suman[left]
                    left += 1
                    right -= 1
        temp = head
        i = 0
        while temp:
            temp.val = suman[i]
            i += 1
            temp = temp.next
        return head