class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        suman = []
        for i in lists:
            while i:
                suman.append(i.val)
                i = i.next
        if not suman:
            return None
        suman.sort()
        head = ListNode(suman[0])
        temp = head
        for i in range(1, len(suman)):
            temp.next = ListNode(suman[i])
            temp = temp.next
        return head