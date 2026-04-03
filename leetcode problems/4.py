"""
4. Median of Two Sorted Arrays
Solved
Hard

Topics

Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""


class Solution:
    """
    Variant 1:
    My first successful attempt at solving this problem, which I was able to arrive at in
    a little over 30 mins. This might be the fastest I ever fully solved a LC Hard problem!
    My educated guess (based on the problem's requirement) is that the time complexity of
    this solution is O(log(m+n)) where m and n are the lengths of nums1 and nums2, and that
    the space complexity of this solution is O(m+n), because of the size of the merged list
    the algorithm must store. However, LC's analysis tool claims that this solution really
    has a time complexity of O(N^2) and a space complexity of O(N), where I am guessing that
    N = m+n, which means I was right about the space complexity but not the time complexity.
    This solution beats only ~6% and ~50% of accepted answers in terms of RT and memory
    efficiency respectively.   
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joined_lists = nums1 + nums2
        #print(joined_lists)
        m = len(nums1)
        merged_len = len(joined_lists)
        for start in range(m, merged_len):
            #print(start)
            while joined_lists[start] < joined_lists[start-1] and start > 0:
                #print('inside')
                big = joined_lists[start-1]
                small = joined_lists[start]
                joined_lists[start-1:start+1] = [small, big]
                start -= 1
                #print(start)

        #print(joined_lists)
        if merged_len%2:
            return joined_lists[merged_len//2]
        else:
            return (joined_lists[int(merged_len/2) - 1] + joined_lists[int(merged_len/2)])/2


class Solution:
    """
    Variant 2:
    The official solution given by LC for 'Approach 1: Merge Sort' to solve this problem.
    According to the complexity analysis covered in the Editorial section, the time
    complexity of this solution is O(m+n) and the space complexity if O(1). LC's analysis
    tool confirms this, clarifying that the time complexity if technically O((m+n)/2). 
    This solution beats ~50% and ~40% of accepted answers in run time and memory efficiency
    respectively. However, I question this figure for the memory efficiency percentile
    since Variant 1 has O(m+n) space complexity and was estimated to beat ~50% of accepted
    answers, while this solution has lower space complexity but is estimated to beat only
    ~40%.
    """
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0

        # Get the smaller value between nums1[p1] and nums2[p2].
        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans

        if (m + n) % 2 == 0:
            for _ in range((m + n) // 2 - 1):
                _ = get_min()
            return (get_min() + get_min()) / 2
        else:
            for _ in range((m + n) // 2):
                _ = get_min()
            return get_min()


class Solution:
    """
    Variant 3:
    My successful reproduction of the official solution for 'Approach 2: Binary Search, 
    Recursive' given by LC to solve this problem. My hypothesis is that the time 
    complexity of this solution is O(log(m+n)) (or O(log('na' + 'nb')) as defined in 
    this code), and the space complexity is O(1). LC's analysis tool claims that this
    submission has O(log(min(na,nb))) complexity in both time and space. However, the 
    Editorial section states that for Approach 2, O(log(m*n)) and O(logm + logn) are the 
    time and space complexities respectively. Here is the Editorial's in-depth explanation:

    -------------------------------------------------------------------------------------

    Complexity Analysis

    Let m be the size of array nums1 and n be the size of array nums2.

    Time complexity: O(log(m⋅n))

    At each step, we cut one half off from either nums1 or nums2. If one of the arrays is 
    emptied, we can directly get the target from the other array in a constant time. 
    Therefore, the total time spent depends on when one of the arrays is cut into an empty 
    array. In the worst-case scenario, we may need to cut both arrays before finding the 
    target element. One of the two arrays is cut in half at each step, thus it takes 
    logarithmic time to empty an array. The time to empty two arrays are independent of 
    each other.

    img

    Therefore, the time complexity is O(logm+logn).
    O(logm+logn)=O(log(m⋅n))
    
    Space complexity: O(logm+logn)

    Similar to the analysis on time complexity, the recursion steps depend on the number 
    of iterations before we cut an array into an empty array. In the worst-case scenario, 
    we need O(logm+logn) recursion steps.

    However, during the recursive self-call, we only need to maintain 4 pointers: a_start, 
    a_end, b_start and b_end. The last step of the function is to call itself, so if tail 
    call optimization is implemented, the call stack always has O(1) records.

    Please refer to Tail Call for more information on tail call optimization.

    -------------------------------------------------------------------------------------

    Tail Call Optimization (TCO) is not natively supported in Python, but converting the 
    recursion to an iterative approach provides the same benefits.

    This solution beats ~50% of accepted answers in RT efficiency but only ~5% in memory
    efficiency.

    Next I will try implementing this same approach iteratively rather than recursively to
    see how much that improves the efficiency.
    """
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        na = len(nums1)
        nb = len(nums2)

        def solve(k, start_a, end_a, start_b, end_b):
            if start_a > end_a:
                return nums2[k-start_a]
            elif start_b > end_b:
                return nums1[k-start_b]
            
            index_a = (end_a + start_a)//2
            index_b = (end_b + start_b)//2

            value_a = nums1[index_a]
            value_b = nums2[index_b]

            if index_a + index_b < k:
                if value_a > value_b:
                    return solve(k, start_a, end_a, index_b+1, end_b)
                else:
                    return solve(k, index_a+1, end_a, start_b, end_b)
            else:
                if value_a > value_b:
                    return solve(k, start_a, index_a-1, start_b, end_b)
                else:
                    return solve(k, start_a, end_a, start_b, index_b-1)

        if (na + nb)%2:
            return solve(int((na+nb-1)/2), 0, na-1, 0, nb-1)
        
        else:
            half = int((na+nb)/2)
            return (solve(half-1, 0, na-1, 0, nb-1) + solve(half, 0, na-1, 0, nb-1))/2


class Solution:
    """
    Variant 4:
    The following is the adaptation of Variant 3 to an iterative implementation, as an
    exercise to simulate TCO. This implementation should have O(1) space complexity,
    but the time complexity should be the same as Variant 3. Let's see if LC's analysis
    tool is able to pick up on this difference: and it is! Now the analysis tool claims
    that the time complexity is still O(Log(Min(Na,Nb))), but the space complexity is 
    now O(1). Awesome, however I still don't know why it thinks that the time complexity
    is O(Log(Min(Na,Nb))) while the Editorial claims it is O(log(m*n)) for Approach 2,
    which this is based off of. Maybe O(Log(Min(Na,Nb))) is the average complexity and
    O(log(m*n)) is the worst case? This solution beats ~60% and ~40% of accepted answers
    in run time and memory efficiency respectively, indicating that this solution is in
    fact superior to Variant 3. 
    """
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        na = len(nums1)
        nb = len(nums2)

        def solve(k, start_a, end_a, start_b, end_b):
            while True:
                if start_a > end_a:
                    return nums2[k-start_a]
                elif start_b > end_b:
                    return nums1[k-start_b]
                
                index_a = (end_a + start_a)//2
                index_b = (end_b + start_b)//2

                value_a = nums1[index_a]
                value_b = nums2[index_b]

                if index_a + index_b < k:
                    if value_a > value_b:
                        start_b = index_b + 1
                    else:
                        start_a = index_a + 1
                else:
                    if value_a > value_b:
                        end_a = index_a - 1
                    else:
                        end_b = index_b - 1

        if (na + nb)%2:
            return solve(int((na+nb-1)/2), 0, na-1, 0, nb-1) 
            
        else:
            half = int((na+nb)/2)
            return (solve(half-1, 0, na-1, 0, nb-1) + solve(half, 0, na-1, 0, nb-1))/2 


class Solution:
    """
    Variant 5:
    The official solution given by LC for 'Approach 3: A Better Binary Search' for solving
    this problem. I have yet to implement this approach myself, however the improvement in
    time complexity from Approach 2 as stated in the Editorial makes sense. Here is the
    complexity analysis for Approach 3 taken straight from the Editorial for this problem:

    --------------------------------------------------------------------------------------

    Complexity Analysis

    Let m be the size of array nums1 and n be the size of array nums2.

    Time complexity: O(log(min(m,n)))

    We perform a binary search over the smaller array of size min(m,n).
    Space complexity: O(1)

    The algorithm only requires a constant amount of additional space to store and update a 
    few parameters during the binary search.

    --------------------------------------------------------------------------------------

    This solution beats ~70% and ~50% of accepted answers in run time and memory efficiency
    respectively.

    """
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = (
                float("-inf") if partitionA == 0 else nums1[partitionA - 1]
            )
            minRightA = float("inf") if partitionA == m else nums1[partitionA]
            maxLeftB = (
                float("-inf") if partitionB == 0 else nums2[partitionB - 1]
            )
            minRightB = float("inf") if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (
                        max(maxLeftA, maxLeftB) + min(minRightA, minRightB)
                    ) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1


