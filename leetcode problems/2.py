"""
2. Add Two Numbers
Solved
Medium

Topics

Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Variant 1:
    My first successful attempt at solving this problem using the first approach that 
    came to mind. My hypothesis is that the time complexity of this solution is O(max(m,n))
    where m and n are the lengths of l1 and l2 respectively, and that the space complexity
    is also O(max(m,n)). Let's see what LC's analysis tool says...
    It reports O(N) for both the time and space complexity. I am not sure what N is, but I
    am guessing it is the length of the linked list l3 that results from evaluating the sum
    of l1 and l2. This solution beats ~35% and ~5% of accepted answers in run time and
    memory efficiency respectively. 
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first construct the string representation of l1
        l1_str = str(l1.val)
        curr = l1
        while curr.next is not None:
            l1_str += str(curr.next.val)
            curr = curr.next

        l1_str = l1_str[::-1]

        # first construct the string representation of l2
        l2_str = str(l2.val)
        curr = l2
        while curr.next is not None:
            l2_str += str(curr.next.val)
            curr = curr.next

        l2_str = l2_str[::-1]

        print(l1_str)

        print(l2_str)

        l3_sum = int(l1_str) + int(l2_str)

        l3_str = str(l3_sum)
        l3_str = l3_str[::-1]

        l3 = ListNode(int(l3_str[0]))

        curr = l3

        for char in l3_str[1:]:
            curr.next = ListNode(int(char))
            curr = curr.next

        return l3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Variant 2:
    My successful attempt at reproducing the approach demonstrated in the Video Solution
    of the Editorial for this problem. According to the video, the run time complexity 
    of this solution is O(max(m,n)) where m and n are the lengths of l1 and l2 
    respectively, while the space complexity is O(1) since the memory required to execute 
    this algorithm does not depend on the size of the input variables except for the space 
    required to construct the new linked list given by 'head' which 'addTwoNumbers' returns.
    According to LC's analysis tool, the complexity is O(N) in both time and space, just
    like Variant 2. Thus Variant 1 and 2 are probably close in terms of run time and
    memory efficiency, but let's see if we can get a better idea of which might be better
    from real performance metrics...
    This solution beats ~50% and ~5% of accepted answers in run time and memory efficiency 
    respectively, which means Variant 2 might be slightly preferable to Variant 1. 
    This approach to solving this problem is pretty intuitive and probably would have been 
    the 2nd one I would have come up with on my own after Variant 1.      
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            z = x + y + carry
            curr.next = ListNode(z%10)
            carry = z//10
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return head.next