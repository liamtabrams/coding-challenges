"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/

1190. Reverse Substrings Between Each Pair of Parentheses
Solved
Medium

Topics

Companies

Hint
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
"""

def find_indices(string, char):
    return [index for index, c in enumerate(string) if c == char]

class Solution:
    """
    Variant 1:
    This solution has a run time complexity of O(n^2), but even compared to other possible solutions that 
    have O(n^2) run time complexity it is extra slow because of the various list comprehensions which we may 
    be able to navigate around. In addition, this has a space complexity of O(n) but compared to other 
    solutions that have space complexity O(n) this solution is likely less efficient in terms of space 
    complexity as well because it may define extra variables that we may be able to get around using.
    """
    def reverseParentheses(self, s: str) -> str:
        while True:
            left_paren_indices = find_indices(s, '(')
            right_paren_indices = find_indices(s, ')')
            if len(left_paren_indices) == len(right_paren_indices) == 0:
                break
            first_right_paren_ind = right_paren_indices[0]
            corresponding_left_paren_ind = [x for x in left_paren_indices if x < first_right_paren_ind][-1]
            inner_phrase = s[corresponding_left_paren_ind + 1 : first_right_paren_ind]
            inner_phrase = inner_phrase[::-1]
            s = s[:corresponding_left_paren_ind] + inner_phrase + s[first_right_paren_ind+1:]
        
        return s

class Solution:
    """
    Variant 2:
    This solution has a run time complexity of O(n^2), and a space complexity of O(n), but compared to 
    Variant 1, it is more efficient in both categories, as it navigates around using some extraneous
    list comprehensions and variables. Conceptually though, it is the same algorithm as Variant 1.
    """
    def reverseParentheses(self, s: str) -> str:
        char_list = [char for index, char in enumerate(s)]
        while True:
            if ')' not in char_list:
                break
            right_paren_index = char_list.index(')')
            for i in range(right_paren_index, -1, -1):
                if char_list[i] == '(':
                    left_paren_index = i
                    break
            inner_phrase = s[left_paren_index + 1 : right_paren_index]
            inner_phrase = inner_phrase[::-1]
            s = s[:left_paren_index] + inner_phrase + s[right_paren_index + 1:]
            char_list.pop(right_paren_index)
            char_list.pop(left_paren_index)
        
        return s

class Solution:
    """
    Variant 3: 
    This is the official solution offered by leetcode. It also has a run time complexity of O(n^2)
    but is indeed more efficient. In terms of space complexity, is has O(n) complexity, and it is 
    not obvious whether it is the same, better, or worse than Variant 2. I would suspect that it is
    also superior in terms of space complexity, since it requires defining fewer variables in the 
    for loop and less redundancy in the string slicing.  
    """
    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        result = []

        for current_char in s:
            if current_char == "(":
                # Store the current length as the start index
                # for future reversal
                open_parentheses_indices.append(len(result))
            elif current_char == ")":
                start = open_parentheses_indices.pop()
                # Reverse the substring between the matching parentheses
                result[start:] = result[start:][::-1]
            else:
                # Append non-parenthesis characters to the processed list
                result.append(current_char)
        return "".join(result)

class Solution:
    """
    Variant 4: 
    The most efficient solution offered by leetcode is the Wormhole Teleportation Technique.
    This is my attempt at reproducing the described solution without referring to the code.

    This solution has a run time complexity of O(n) and a space complexity of O(n) as well. 
    So clearly it is the superior approach to this problem in terms of runtime, but I also 
    supsect it is superior in terms of spatial complexity because no variables are defined
    within the loops themselves.  
    """
    def reverseParentheses(self, s: str) -> str:
        open_paren_indices = []
        result = ''
        pair_dict = {}
        index = 0
        for char in s:
            if char == '(':
                open_paren_indices.append(index)
            elif char == ')':
                matching_paren_index = open_paren_indices.pop(-1)
                pair_dict[index] = matching_paren_index
                pair_dict[matching_paren_index] = index
            index += 1
        
        index = 0
        direction = 1
        while True:
            if len(result) + len(pair_dict.keys()) == len(s):
                break
            if s[index] not in ['(', ')']:
                result += s[index]
            elif s[index] == '(':
                index = pair_dict[index]
                direction *= -1
            else:
                index = pair_dict[index]
                direction *= -1
            index += direction
        
        return result
            

class Solution:
    """
    Variant 5: 
    The official solution offered by leetcode for the Wormhole technique. 
    Before looking at it I suspect they used something besides a dictionary to store the
    bidirectionally linked parentheses pairings, so that may make it slightly more efficient
    than my implementation. Update: I think we'd need to test this out with large strings to
    really see which is better because it's really not obvious. It may come as no surprise 
    that I find my solution to be more intuitive (which often results in less efficiency).

    This solution has a run time complexity of O(n) and a space complexity of O(n) as well. 
    So clearly it is the superior approach to this problem in terms of runtime, but I also 
    supsect it is superior in terms of spatial complexity because no variables are defined
    within the loops themselves.  
    """
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n

        # First pass: Pair up parentheses
        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i

        # Second pass: Build the result string
        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index += direction

        return "".join(result)


class Solution:
    """
    Variant 6:
    A new approach I have gotten to work coming back to the problem over a week after
    the first time I solved it. It involves getting the indices of the closing
    parentheses in the original string, then iterating over each of those indices to move 
    backward to find the closest open parenthesis which must correspond to it after 
    directly modifying s and removing each previously found pair of parentheses, using an 
    accumulator variable to keep track of the correct indices of the remaining closing
    parentheses in s, then returning s after iterating over the whole closed_indices
    list. Even though the run time complexity is technically O(N^2), this particular
    solution beats ~50% of accepted answers in terms of time efficiency. As with all the
    other variants the space complexity if O(N).
    """   
    def reverseParentheses(self, s: str) -> str:
        #open_indices = []
        closed_indices = []
        for index, char in enumerate(s):
            #if char == '(':
                #open_indices.append(index)
            if char == ')':
                closed_indices.append(index)

        acc = 0
        for item in closed_indices:
            print(s)
            for j in range(1, item - acc + 1):
                if s[item - acc - j] == '(':
                    s = s[:item - acc - j] + s[item - acc - j + 1: item - acc][::-1] + s[item - acc + 1:]
                    acc += 2
                    break

        return s



            
