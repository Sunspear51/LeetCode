#!/usr/bin/env python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        def reverseLinkedList(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        def getLength(head):
            length = 0
            current = head
            while current:
                length += 1
                current = current.next
            return length

        length = getLength(head)

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        current = head

        while length >= k:
            group_start = current
            group_end = current

            for _ in range(k - 1):
                group_end = group_end.next

            next_group_start = group_end.next
            group_end.next = None

            prev_group_end.next = reverseLinkedList(group_start)
            group_start.next = next_group_start
            prev_group_end = group_start
            current = next_group_start
            length -= k

        return dummy.next