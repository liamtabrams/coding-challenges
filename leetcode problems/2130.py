"""
2130. Maximum Twin Sum of a Linked List
Solved
Medium
Topics
Companies
Hint
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """
    Variant 1:
    My first successful attempt at solving this problem and the very obvious/intuitive
    approach. This solution has a time complexiy of O(n) (where n is the number of nodes
    in the linked list given by 'head') and a space complexity of O(n) as well. LC's 
    analysis tool confirms this. This solution beats ~40% and ~25% of accepted answers 
    in terms of RT and memory efficiency respectively. This suggests there are substantially 
    better solutions out there.
    """
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 2
        curr = head
        vals_list = []
        vals_list.append(curr.val)
        while curr.next is not None:
            curr = curr.next
            vals_list.append(curr.val)

        '''if half the list length is odd, such as 3, the first twin starting from center moving left
        has index 2, and if half the list length is even, such as 4, the first twin starting from 
        center moving left has index 3'''
        left_twin_index = int(len(vals_list)/2 - 1)
        right_twin_index = int(len(vals_list)/2)
        shift_pos = 0
        while shift_pos < int(len(vals_list)/2):
            twin_sum = vals_list[left_twin_index-shift_pos] + vals_list[right_twin_index+shift_pos]
            if twin_sum > max_sum:
                max_sum = twin_sum
            shift_pos += 1
        
        return max_sum


class Solution(object):
    """
    Variant 2:
    The official solution given by LC for 'Approach 1: Using List Of Integers'. This is
    essentially the same approach as what I initially came up with (Variant 1) but uses
    slightly different logic, and a max method to compare a given twin sum to the current
    maximum sum being stored, rather than a comparison operator to decide whether to 
    update the maximum sum being stored. Also, in the second while loop, the two index
    pointers start off at the beginning and end of the values list and work inward, rather 
    than starting from the innermost twin indices and working outward. This implementation
    would evidently also have O(n) complexity in both time and space. It performs roughly
    the same as Variant 1 in terms of measurable RT and memory efficiency (~40% and ~25%
    respectively).
    """
    def pairSum(self, head):
        current = head
        values = []

        while current:
            values.append(current.val)
            current = current.next
        
        i = 0
        j = len(values) - 1
        maximumSum = 0
        while(i < j):
            maximumSum = max(maximumSum, values[i] + values[j])
            i = i + 1
            j = j - 1
        
        return maximumSum


class Solution(object):
    """
    Variant 3:
    The official solution given by LC for 'Approach 2: Using Stack'. This solution has a
    time complexity of O(n) and space complexity of O(n) as well. Instead of using two
    index pointers to find corresponding twin values to calculate the twin sums in the 
    2nd while loop, items are popped from the values list we created with the 1st while
    loop (which is called 'st') as we traverse the linked list starting from head using 
    the 2nd while loop, in order to calculate the twin sums so we can find the maximum sum.
    This particular solutions beats only ~30% and ~20% of accepted answers in terms of RT
    and memory efficiency, so I don't really see the appeal over Approach 1.
    """
    def pairSum(self, head):
        current = head
        st = []
        maximumSum = 0

        while current:
            st.append(current.val)
            current = current.next

        current = head
        size = len(st)
        count = 1
        maximumSum = 0
        while count <= size/2:
            maximumSum = max(maximumSum, current.val + st.pop())
            current = current.next
            count = count + 1

        return maximumSum


class Solution(object):
    """
    Variant 4:
    My successful attempt at reproducing 'Approach 3: Reverse Second Half In Place' given
    by LC. The run time complexity of this solution is O(n) and the space complexity is O(1),
    as confirmed by LC's analysis tool. This solution beats ~87% and ~69% of accepted answers
    in terms of RT and memory efficiency. Let's see how these figures compare to the official
    implementation of Approach 3 given by LC.
    """ 
    def pairSum(self, head):
        slow = head
        fast = head.next
        max_sum = 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        prev, curr = None, slow
        while curr:
            old_next = curr.next
            curr.next = prev
            prev = curr
            curr = old_next

        twin1 = head
        twin2 = prev

        while twin1 and twin2:
            twin_sum = twin1.val + twin2.val
            if twin_sum > max_sum:
                max_sum = twin_sum
            twin1 = twin1.next
            twin2 = twin2.next

        return max_sum


class Solution(object):
    """
    Variant 5:
    The official solution for 'Approach 3: Reverse Second Half In Place' given by LC. It
    has time and space complexity of O(n) and O(1) respectively. It rather cleverly finds
    what would be the head of the second half of the linked list and then works backwards
    to construct that second half linked list in reverse. Then, it takes the original
    linked list and the reversed second half of the original linked list and traverses both
    simultaneously one node at a time to calculate the twin sums. This solution appears to 
    beat ~70% and 65% of accepted answers in terms of RT and memory efficiency respectively,
    suggesting my implementation in Variant 4 is slightly more optimal than this one. I am
    not sure why that might be, but one hypothesis is that the assignment of the return
    value of the max function to the maximumSum variable might add a bit of overhead to the
    algorithm as compared to just using the comparison operator to decide whether to update
    that variable like Variant 4 does. More investigation would be needed to validate that
    hypothesis. 
    """
    def pairSum(self, head):
        slow, fast = head, head
        maximumSum = 0

        # Get middle of the linked list.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half of the linked list.
        curr, prev = slow, None
        while curr:       
            curr.next, prev, curr = prev, curr, curr.next
        
        start = head
        while prev:
            maximumSum = max(maximumSum, start.val + prev.val)
            prev = prev.next
            start = start.next

        return maximumSum