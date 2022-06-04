class Solution:
    def mergeKLists(self, lists):
        
        lst = []
        for l in lists:
            c = l
            while c is not None:
                lst.append(c.val)
                c = c.next
        lst.sort()
        
        head = ListNode(0)
        previous = head
        for l in lst:
            node = ListNode(l)
            previous.next = node
            previous = previous.next
            
        return head.next

