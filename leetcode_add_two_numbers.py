class Solution:
    def addTwoNumbers(self, l1, l2):
        sum = 0
        l1_current = l1
        l2_current = l2
        new_node = ListNode()
        head = ListNode(0)
        previous = head
        while l1_current is not None or l2_current is not None or sum != 0:
            if l1_current is not None:
                sum += l1_current.val
                l1_current = l1_current.next
            if l2_current is not None:
                sum += l2_current.val
                l2_current = l2_current.next
            print("sum" , sum)
            node = ListNode(sum%10)
            sum //= 10
            previous.next = node
            previous = previous.next
            
        return head.next
            
        # res_node = ListNode()
