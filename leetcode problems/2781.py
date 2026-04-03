"""
2781. Length of the Longest Valid Substring
Solved
Hard

Topics

Companies
You are given a string word and an array of strings forbidden.

A string is called valid if none of its substrings are present in forbidden.

Return the length of the longest valid substring of the string word.

A substring is a contiguous sequence of characters in a string, possibly empty.

 

Example 1:

Input: word = "cbaaaabc", forbidden = ["aaa","cb"]
Output: 4
Explanation: There are 11 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", "ab", "abc" and "aabc". The length of the longest valid substring is 4. 
It can be shown that all other substrings contain either "aaa" or "cb" as a substring. 
Example 2:

Input: word = "leetcode", forbidden = ["de","le","e"]
Output: 4
Explanation: There are 11 valid substrings in word: "l", "t", "c", "o", "d", "tc", "co", "od", "tco", "cod", and "tcod". The length of the longest valid substring is 4.
It can be shown that all other substrings contain either "de", "le", or "e" as a substring. 
 

Constraints:

1 <= word.length <= 105
word consists only of lowercase English letters.
1 <= forbidden.length <= 105
1 <= forbidden[i].length <= 10
forbidden[i] consists only of lowercase English letters.
"""


class Solution:
    """
    Variant 1:
    I spent a couple of hours trying to come up with an elegant solution to this problem 
    on my own but was unsuccessful. So I eventually referred to the following solution from
    Cat and Tea under the Solutions section: 
    https://leetcode.com/problems/length-of-the-longest-valid-substring/solutions/3771333/picture-short-and-concise-approach-easy-to-understand-in-depth-explanation/

    After some mental weight lifting I was able to understand Cat and Tea's solution but not 
    well enough to be able to write the implementation on my own my first few attempts. I
    lost a bit of my drive and ended up comparing my code to the solution's side by side to
    get my implementation working, rather than actually debugging my code on my own. 

    My educated guess is that the RT complexity of this solution is O((N*M)logM) where N is
    the length of the input 'word' and M is the length of the input 'forbidden', and that 
    the space complexity is O(M). However, LC's analysis tool reports O(N*M) and O(M). So I
    was correct about the space complexity and at least came close for my guess for the time
    complexity. I think the time complexity does depend on whether or not forbidden is sorted.


    """
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        right_pointer = len(word) - 1
        res = 0
        for left_pointer in range(len(word) - 1, -1, -1):
            for k in range(left_pointer, min(left_pointer+10, right_pointer+1)):
                if word[left_pointer:k+1] in forbidden_set:
                    right_pointer = k - 1
                    break
            res = max(res, right_pointer - left_pointer + 1)

        return res