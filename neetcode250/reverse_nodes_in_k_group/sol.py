# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def recurse(j, head):
            if j == 1:
                return (head, head.next, head)
            if not head.next:
                return None
            next_pair = recurse(j-1, head.next)
            if next_pair: 
                next_node = next_pair[0]
                next_seq = next_pair[1]
                new_head = next_pair[2]
    
                next_node.next = head
                head.next = next_seq
    
                return (head, next_seq, new_head)
            else: return None

        run = recurse(k, head)
        new_head = run[2] if run else head
        while run and run[1]:
            old_tail = run[0]
            run = recurse(k, run[1])
            if run:
                old_tail.next = run[2]
        return new_head
        # we must return head + ik - 1


        
