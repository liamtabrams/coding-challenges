"""
5. Longest Palindromic Substring
Attempted
Medium

Topics

Companies

Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""


class Solution:
    """
    Variant 1:
    Extremely rough and dirty approach that I got working in less than an hour! It's not
    pretty or a good solution but I am proud of myself for sticking with it and getting
    this approach to work. It's for sure hard to follow/read this code. My first guess
    is that the run time complexity of this solution is O(N^2). My first guess is that
    the space complexity is O(1). This particular solution beats only ~6% of accepted
    answers in terms of time efficiency but ~70% of accepted answers in terms of memory
    efficiency. Leetcode confirmed that my guesses for the run time and space complexity
    were correct.
    """
    def longestPalindrome(self, s: str) -> str:
        len_pal = len(s)
        found = False
        while True:
            if found:
                break
            if len_pal == 1:
                pal_info = [0, len_pal]
                break
            i = len_pal - 1
            j_shift = 0
            while i <= len(s) - 1:
                for j in range(int(round(len_pal/2))):
                    if s[i - j] != s[j + j_shift]:
                        break
                    elif j == int(round(len_pal/2)) - 1:
                        pal_info = [i, len_pal]
                        found = True
                        break
                i += 1
                j_shift += 1
                if found:
                    break
            len_pal -= 1
        
        end_ind, len_pal = pal_info
        return s[end_ind + 1 - len_pal: end_ind + 1]


class Solution:
    """
    Variant 2:
    My first successful attempt at reproducing Approach 1: 'Check All Substrings' given
    by leetcode, which is the brute-force approach. It took me many tries to remove all
    the bugs to get this implementation to pass all test cases. In the worst case I would 
    guess that this solution is bounded by O(n^3) however it beats Variant 1 in real time 
    efficiency (by beating ~30% of accepted answers rather than ~6%), so my guess is 
    probably either incorrect or the ammortized run time is much closer to O(n^2). In terms 
    of space complexity, I think this solution has O(1) space complexity just like Variant 1, 
    and the memory efficiency of this solution beats about ~60% of accepted answers. Leetcode
    analyzed this particular solution to have O(n^2) and O(1) complexity in time and space,
    respectively. Comparing my solution to the official solution for 'Check All Substrings'
    given by leetcode, I unnecessarily used an additional variable 'acc' in my logic for
    calling the 'check' function, and I return s[0] if 'check' never returns True rather than
    "".
    """
    def longestPalindrome(self, s: str) -> str:
        
        def check(s, m, n):
            while m < n:
                if s[m] != s[n]:
                    return False
                m+=1
                n-=1
            return True
        
        acc = 0
        for j in range(len(s) - 1, 0, -1):
            for i in range(acc + 1):
                if check(s, i, j + i):
                    return s[i:j+i+1]
            acc += 1
    
        return s[0]


class Solution:
    """
    Variant 3:
    The official solution for Approach 1: 'Check All Substrings' given by leetcode, which
    is the brute-force approach. This particular solution beats ~28% of accepted answers
    in terms of time efficiency and ~60% of accepted answers in terms of memory efficiency.
    It's almost identical to Variant 2 and was analyzed by leetcode to have O(n^2) and O(1)
    complexity in time and space respectively. It turns out that my hypothesis about the
    run time complexity in the worst case being O(n^3) was actually correct, but the
    editorial for this problem explains that 'Due to the optimizations of checking the 
    longer length substrings first and exiting the palindrome check early if we determine 
    that a substring cannot be a palindrome, the practical runtime of this algorithm is not
    too bad.
    """
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start : start + length]

        return ""


import numpy as np

class Solution:
    """
    Variant 4:
    My first successful attempt at reproducing Approach 2: 'Dynamic Programming' given
    by leetcode. It took me hours to try to do this without looking at the code and
    rereading the description of this method; finally I gave up and looked at the code
    which was simpler than I was expecting, and it came as no shocker that I hadn't been
    thinking about or applying the stated strategy correctly. My first guess at run time 
    and space complexity of this approach is O(n^2) for both. Leetcode confirms my guess
    is accurate. This particular solution beats only ~27% of accepted answers in time 
    efficiency and ~6% in memory efficiency. 
    """ 
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        info_matrix = np.zeros((n,n))
        longest_pal = s[0]
        for i in range(n):
            info_matrix[i][i] = 1
            if i < (n - 1) and s[i] == s[i+1]:
                # this will enforce all 1's to be above the diagonal
                info_matrix[i][i+1] = 1
                longest_pal = s[i:i+2]

        for dist in range(2,n):
            for i in range(n - dist):
                j = i + dist
                if s[i] == s[j] and info_matrix[i+1][j-1]:
                    info_matrix[i][j] = 1
                    longest_pal = s[i:j+1]

        return longest_pal


class Solution:
    """
    Variant 5: 
    The official solution for Approach 2: 'Dynamic Programming' given by leetcode. This 
    appears to be a slightly more time and space efficient implementation of Approach 2 
    than Variant 4 (my attempt), given it beats ~39% and ~12% of accepted answers in time 
    and space efficiency respectively. I think part of the reason is
    that instead of keeping track of a 'longest_pal' and assigning it new values every 
    time the condition 'if s[i] == s[j] and dp[i + 1][j - 1]' is met, this solution keeps
    track of the last values of i and j with 'ans' and then 'ans' is referenced at the very 
    end to get the values of i and j for the longest palindrome. This saves space and time.
    Still, the order of complexity of this solution in both time and space is O(n^2).
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]


class Solution:
    """
    Variant 6:
    My own successful implementation of Approach 3: 'Expand From Centers' given by
    leetcode. I like this solution a lot because it is the most efficient, elegant,
    intuitive and by far the quickest to write of any I've tried. This is a good lesson
    for me that the best answers to leetcode problems are typically elegant and clean 
    to write. I would guess that it the time complexity is O(n^2) since we call the expand
    function, which has the while loop where we expand from i and j, within a for
    loop for values in the range of the length of the string. I would also guess that the 
    space complexity is O(n) for this implementation, since we are storing the longest_pal 
    string while the whole algorithm runs. Technically we could just be storing index and 
    length values for the longest palidrome found so far, and I think that would get our 
    space complexity down to O(1). Leetcode agrees with me on the run time compexity being
    O(n^2) but thinks the space complexity of this particular implementation is still O(1).
    Also, this particular solution beats ~47% and ~55% of accepted answers in terms of time
    and memory efficiency respectively.  
    """
    def longestPalindrome(self, s: str) -> str:
        longest_pal = s[0]

        # function to return longest palindrome from expanding from i and j
        def expand(i, j):
            # THE CASE WHERE THE CANDIDATE PALINDROME HAS EVEN LENGTH
            found = False
            pal = None
            while i >= 0 and j <= len(s) - 1:
                if s[i] == s[j]:
                    pal = s[i:j+1]
                    found = True
                    i -= 1
                    j +=1
                else:
                    break
                
            return [found, pal]


        for i in range(len(s) - 1):
            ans = expand(i, i)
            if ans[0]:
                if len(ans[1]) > len(longest_pal):
                    longest_pal = ans[1]
            
            if i != len(s) - 1:
                ans = expand(i, i+1)
                if ans[0]:
                    if len(ans[1]) > len(longest_pal):
                        longest_pal = ans[1]

        return longest_pal


class Solution:
    """
    Variant 7:
    The official solution for Approach 3: 'Expand From Centers' given by leetcode, which
    states that 
    
    "Although the time complexity is the same as in the DP approach, the 
    average/practical runtime of the algorithm is much faster. This is because most 
    centers will not produce long palindromes, so most of the O(n) calls to expand will 
    cost far less than n iterations." 
    
    Since this algorithm doesn't use any extra space except a few integers, the
    editorial is correct in saying that the space complexity is O(1). However I do think 
    it misanalyzed my implementation which is less space efficient. I do think it is
    also more time-efficient than Variant 6 because it does not have to lookup the length
    of the currently longest found palindrome every time 'expand' returns a non-None 
    answer. Instead it more directly keeps track of the indices of the boundaries for
    the longest palindrome found (and thus length), replacing lookup time with basic
    arithmetic. This solution beats ~85% of accepted answers in time efficiency and ~65%
    in memory efficiency. 

    """
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        ans = [0, 0]

        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i : j + 1]


class Solution:
    """
    Variant 8:
    This is the official solution given by leetcode for Approach 4: 'Manacher's Algorithm'.
    I have not (yet) been able to write my own implementation using this strategy, but 
    hopefully it will come. This solution is not particularly intuitive or elegant like
    Approach 3 but it is the best solution in terms of run time complexity, with O(n)
    complexity. In terms of space complexity it is not the best since it has O(n), rather
    than O(1), complexity. This solution beats ~97% of accepted answers in terms of run
    time efficiency and ~60% of accepted answers in terms of memory efficiency. Overall it
    is the best solution but the hardest to devise.
    """ 
    
    def longestPalindrome(self, s: str) -> str:
        s_prime = "#" + "#".join(s) + "#"
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0

        for i in range(n):
            mirror = 2 * center - i

            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

            while (
                i + 1 + palindrome_radii[i] < n
                and i - 1 - palindrome_radii[i] >= 0
                and s_prime[i + 1 + palindrome_radii[i]]
                == s_prime[i - 1 - palindrome_radii[i]]
            ):
                palindrome_radii[i] += 1

            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]

        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index : start_index + max_length]

        return longest_palindrome


class Solution:
    """
    Variant 9:
    My successful attempt at reimplementing Approach 4: 'Manacher's Algorithm' given by
    leetcode on my own. This implementation is slightly worse/less elegant than Variant 8 
    given the unnecessary logic I used at the end of the function to convert the info from 
    palindrome_radii into the correct left and right indices needed to slice the original
    string s. I didn't realize on my own that the following four lines:
     
     max_length = max(palindrome_radii)
     center_index = palindrome_radii.index(max_length)
     start_index = (center_index - max_length) // 2
     longest_palindrome = s[start_index : start_index + max_length]

    will work for both even and odd cases. 
    
    The time and space complexity of this solution are both O(N). This solution beats ~97% 
    of accepted answers in terms of run time efficiency and ~24% of accepted answers in 
    terms of memory efficiency. Honestly I don't have a very confident explanation for why 
    this particular implementation is so much less memory efficient than Variant 8, but it 
    might be because I am using one additional variable to store the value of the upper_index
    of the substring returned, rather than slicing s this way:
    
    longest_palindrome = s[start_index : start_index + max_length]

    , which does not use the extra variable:
    """ 
    def longestPalindrome(self, s: str) -> str:
        s_prime = '#' + '#'.join(s) + '#'
        print(s_prime)
        radius = center = 0
        n = len(s_prime)
        palindrome_radii = [0 for i in range(n)]
        print(palindrome_radii)
        for i in range(n):
            mirror = 2*center - i
            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])
            while i + palindrome_radii[i] + 1 < n and i - palindrome_radii[i] - 1 >= 0 and s_prime[i+palindrome_radii[i]+1] == s_prime[i-palindrome_radii[i]-1]:
                palindrome_radii[i] += 1
            if i + palindrome_radii[i] > radius:
                radius = i + palindrome_radii[i]
                center = i

        max_val = max(palindrome_radii)
        prime_index = palindrome_radii.index(max_val)

        # different cases for even and odd
        if s_prime[prime_index] == '#':
            # we know the palindrome is even
            # then prime_index/2 will give index of first char to right of center in original s
            # in the even case the max_val will give the exact length of our palindrome of interest. Thus the exclusive end index of palindrome within the original string s is int(prime_index/2 + max_val/2)
            upper_ind = int(prime_index/2 + max_val/2)
            lower_ind = upper_ind - max_val 
            return s[lower_ind:upper_ind]
        else:
            # we know the palindrome is odd
            # in this case prime_index//2 = s_index, and max_val also corresponds to the length of the palindrome
            upper_ind = int(prime_index//2 + max_val//2 + 1)
            lower_ind = upper_ind - max_val
            return s[lower_ind:upper_ind]





