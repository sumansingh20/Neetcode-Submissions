class Node:
    def __init__(self,v):
        self.val=v
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def get(self,i):
        cur=self.head
        while cur and i:
            cur=cur.next
            i-=1
        return cur.val if cur else -1

    def insertHead(self,v):
        n=Node(v)
        n.next=self.head
        self.head=n

    def insertTail(self,v):
        n=Node(v)
        if not self.head:
            self.head=n
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=n

    def remove(self,i):
        if not self.head: return False
        if i==0:
            self.head=self.head.next
            return True
        cur=self.head
        while cur.next and i-1:
            cur=cur.next
            i-=1
        if not cur.next: return False
        cur.next=cur.next.next
        return True

    def getValues(self):
        res=[]
        cur=self.head
        while cur:
            res.append(cur.val)
            cur=cur.next
        return res