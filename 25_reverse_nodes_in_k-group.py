from typing import List, Optional
from functools import *
from math import *
from collections import defaultdict
from test_harness.harness import harness_run

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        numNodes = 0
        h = head
        while h:
            numNodes += 1
            h = h.next
        
        h = head
        dummy = past_head = ListNode(0, h) # dummy
        while numNodes >= k:
            print(numNodes)
            numNodes -= k
            # reverse k nodes
            front = h
            prev = None
            for i in range(k):
                tmp = h.next
                h.next = prev
                prev = h
                h = tmp
            front.next = h
            past_head.next = prev
            past_head = front
        
        return dummy.next
            
