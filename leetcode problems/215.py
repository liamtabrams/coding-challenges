"""
215. Kth Largest Element in an Array
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

class Solution:
    """
    Variant 1:
    My very first submission to solve this problem. Obviously, this is the trivial
    solution and not the one of interest, since the problem asks 'Can you solve it
    without sorting?' Nevertheless, this was acceptable. I am guessing that the run time
    complexity of this solution is O(n*logn) where n is the length of 'nums', which comes
    from the sorting. I am guessing that the memory complexity is O(n). Leetcode analyzed
    this solution to have O(nlogn) and O(1) complexity for run time and memory 
    respectively; I was mistaken in thinking the memory complexity is O(n) since there
    isn't an additional variable used by this solution, and it instead reassigns nums 
    sorted to itself. This solution beats ~85% and ~22% of accepted answers in terms of 
    run time and memory efficiency respectively.  
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-1*k]


class Solution:
    """
    Variant 2:
    The official solution for Python3 given by Leetcode for 'Approach 1: Sort'. It's the
    same approach as Variant 1 but a different implementation. Like the above, this 
    solution has O(nlogn) and O(1) complexity in time and space respectively, but based on
    my observations is slightly less efficient in terms of run time than Variant 1, beating
    ~70% and 22% of accepted answers in run time and memory efficiency respectively.
    """
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]


class Solution:
    """
    Variant 3:
    The official solution given by Leetcode for 'Approach 2: Min-Heap'. This solution
    utilizes Python's standard library methods for constructing a heap data structure
    from a list and pushing or popping elements to or from this list. A heap is a binary 
    tree where the value of a parent is always less than the value of its children. Thus, 
    the value at the top of the tree is always the minimum of the list of elements comprising
    it. So we have a very simple approach that builds this heap data structure and
    removes the root node every time the number of elements in the heap exceeds k. After
    this process is done, we have a list where the first element is the kth largest
    element in 'nums'. I am guessing that the run time complexity of this solution is 
    O(n*k) where n is the length of nums, since for each number in nums, we might have
    in the worst case O(k) time complexity for the push to the heap (since there will be at
    most k elements in the heap). I am guessing that the space complexity of this solution
    is O(n) since we need to construct the new representation of 'nums' via heapq. Leetcode 
    states that the time complexity is actually O(nlogk), since operations on a heap cost
    logarithmic time relative to its size. Technically, this is an improvement on Approach
    1 (Variant 2) since k is less than or equal to n. My guess on the space complexity was
    correct. Strangely enough, the efficiency metrics suggest that this solution is worse
    than both Variant 1 and 2, as it beats only ~40% and ~22% of accepted answers.
    """
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]


class Solution:
    """
    Variant 4:
    My successful attempt at implementing 'Approach 3: Quickselect' given by Leetcode.
    When I was thinking about the nontrivial solution to this problem, my mind went to
    quicksort, since the trivial solution involves simply reverse sorting 'nums' and 
    returning the kth element of that sorted list. I was thinking that a reimplementation
    of quicksort where once the list containing the elements greater than the chosen
    pivot for a given iteration reaches k length, we can then sort that list and return
    the kth largest element. However, the way I implemented my strategy was too
    inefficient for Leetcode to be able to evaluate ('Time Limit Exceeded') and I did not
    arrive at the correct approach on my own. This solution is what I wish I had thought
    of on my own! Anyway, without looking at what the Editorial says, my guess is that
    the run time complexity of this solution is O(nlogn) where n is the length of nums,
    and that the space complexity of this solution is also O(nlogn). Now to see if my
    guesses are correct...

    According to the Editorial section: the run time complexity for this approach is O(n)
    on average and O(n^2) in the worst case. The space complexity of this solution is O(n).  
    This seems not necessarily accurate, given that analytically it is a more efficient
    algorithm than Variants 1-3 and when Leetcode analyzes this solution, it reports O(n) 
    and O(1) for the run time and memory efficiency respectively, and yet, the performance 
    metrics suggest it is far LESS efficient than Variants 1, 2, or 3, beating only ~5% of
    accepted answers in terms of run time and memory efficiency. 
    """
    def findKthLargest(self, nums, k):
        def quickselect(items, k):
            pivot = items[0]
            left = []
            mid = []
            mid.append(pivot)
            right = []
            for num in items[1:]:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if k <= len(left):
                return quickselect(left, k)
            elif len(left) + len(mid) < k:
                return quickselect(right, k - len(left) - len(mid))
            else:
                return pivot

        return quickselect(nums, k)


class Solution:
    """
    Variant 5:
    The official solution for 'Approach 3: Quickselect' given by Leetcode. Strangely
    enough, it's the same strategy as the one used in Variant 4, but it performs
    much better, beating ~94% and 10% of accepted solutions in terms of run time and
    memory efficiency respectively. Also strange, but when I had Leetcode analyze
    the complexity of this code after clicking 'Submit', it came up with O(n) for the
    space complexity rather than O(1) which is what it came up with for Variant 4. The
    reason for the huge difference in real performance metrics between this 
    implementation and Variant 4 lies in the choice of pivot in the quick_select 
    function. In my implementation, I chose the first element of the list which for the
    test input used by Leetcode, results in a much longer call stack and a much longer
    run time. In this implementation, the pivot is chosen at random. As for why
    Leetcode analyzed this solution as having O(n) run time while it gave O(1) for my
    implementation is still a mystery, but I don't think O(1) is accurate since Variant
    4 shows worse memory efficency than this one, which has supposedly O(n) complexity.
    """
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if k <= len(left):
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)