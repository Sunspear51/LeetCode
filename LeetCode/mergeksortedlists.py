#!/usr/bin/env python3
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
    
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i))
                lists[i] = head.next
    
        dummy = ListNode()
        current = dummy
    
        while min_heap:
            val, list_index = heapq.heappop(min_heap)
        
            current.next = ListNode(val)
            current = current.next
        
            if lists[list_index]:
                heapq.heappush(min_heap, (lists[list_index].val, list_index))
                lists[list_index] = lists[list_index].next
    
        return dummy.next

    def lists_to_linked_lists(arrays):
        result = []
        for array in arrays:
            dummy = ListNode()
            current = dummy
            for val in array:
                current.next = ListNode(val)
                current = current.next
            result.append(dummy.next)
        return result

    def linked_list_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result