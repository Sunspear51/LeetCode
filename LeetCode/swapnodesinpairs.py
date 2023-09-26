#!/usr/bin/env python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = dummy
    
        while current.next and current.next.next:
            node1 = current.next
            node2 = current.next.next
        
            prev.next = node2
            node1.next = node2.next
            node2.next = node1
        
            prev = node1
            current = node1
    
        return dummy.next