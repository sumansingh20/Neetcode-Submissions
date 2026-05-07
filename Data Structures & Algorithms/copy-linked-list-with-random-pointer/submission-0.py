class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        suman = {}
        temp = head
        while temp:
            suman[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            suman[temp].next = suman.get(temp.next)
            suman[temp].random = suman.get(temp.random)
            temp = temp.next
        return suman[head]