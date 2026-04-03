"""
1717. Maximum Score From Removing Substrings
Solved
Medium

Topics

Companies

Hint
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
"""

class Solution:
    """
    Variant 1:
    The initial solution I got to work for this problem. I believe this has
    a run time complexity of O(N^2) since I am splitting and joining strings
    in a while True loop which could keep running at worst case bounded by N
    times. At first I believed that the space complexity is O(N) since the 
    additional space required for the split string list is bounded by N. 
    However, leetcode analyzed my solution to have space complexity O(1) which
    is better than I thought. 
    
    How can I improve my solution to make it faster, since it only beats 5%
    of accepted answers...? 
    """
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points_gained = 0
        if x > y:
            while True:
                len_s_prior = len(s)
                s = ''.join(s.split('ab'))
                if len(s) == len_s_prior:
                    break
                else:
                    points_gained += (len_s_prior - len(s))*x/2
            while True:
                len_s_prior = len(s)
                s = ''.join(s.split('ba'))
                if len(s) == len_s_prior:
                    break
                else:
                    points_gained += (len_s_prior - len(s))*y/2
            
        else:
            while True:
                len_s_prior = len(s)
                s = ''.join(s.split('ba'))
                if len(s) == len_s_prior:
                    break
                else:
                    points_gained += (len_s_prior - len(s))*y/2
            while True:
                len_s_prior = len(s)
                s = ''.join(s.split('ab'))
                if len(s) == len_s_prior:
                    break
                else:
                    points_gained += (len_s_prior - len(s))*x/2

        return int(points_gained)


class Solution:
    """
    Variant 2:
    My reproduction of Approach 1 given by leetcode, called 'Greedy Way (Stack)'.
    This has time complexity O(n) and space complexity of O(n) as well. 
    """
    def maximumGain(self, s: str, x: int, y: int) -> int:
        num_points = 0
        stack = []
        len_s_prior = len(s)
        if x > y: #we will do 'ab' first
            for char in s:
                if len(stack):
                    if stack[-1] + char == 'ab':
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            s = ''.join(stack)
            num_points += (len_s_prior - len(s))*x/2
            len_s_prior = len(s)
            stack = []
            for char in s: #now we will do 'ba'
                if len(stack):
                    if stack[-1] + char == 'ba':
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            s = ''.join(stack)
            num_points += (len_s_prior - len(s))*y/2

        else: #we will do 'ba' first
            for char in s:
                if len(stack):
                    if stack[-1] + char == 'ba':
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            s = ''.join(stack)
            num_points += (len_s_prior - len(s))*y/2
            len_s_prior = len(s)
            stack = []
            for char in s: #now we will do 'ba'
                if len(stack):
                    if stack[-1] + char == 'ab':
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            s = ''.join(stack)
            num_points += (len_s_prior - len(s))*x/2
        
        return int(num_points)


class Solution:
    """
    Variant 3:
    The official solution given by leetcode for Approach 1: 'Greedy Way (Stack)'.
    Both the time and space complexity of this solution is O(n).
    """
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_points = 0
        s = list(s)

        if x > y:
            # Remove "ab" first (higher points), then "ba"
            total_points += self.remove_substring(s, "ab", x)
            total_points += self.remove_substring(s, "ba", y)
        else:
            # Remove "ba" first (higher or equal points), then "ab"
            total_points += self.remove_substring(s, "ba", y)
            total_points += self.remove_substring(s, "ab", x)

        return total_points

    def remove_substring(
        self, input_string, target_substring, points_per_removal
    ):
        total_points = 0
        write_index = 0

        # Iterate through the string
        for read_index in range(0, len(input_string)):
            # Add the current character
            input_string[write_index] = input_string[read_index]
            write_index += 1

            # Check if we've written at least two characters and
            # they match the target substring
            if (
                write_index > 1
                and input_string[write_index - 2] == target_substring[0]
                and input_string[write_index - 1] == target_substring[1]
            ):
                write_index -= 2
                total_points += points_per_removal

        # Trim the list to remove any leftover characters
        del input_string[write_index:]

        return total_points



class Solution:
    """
    Variant 4:
    The official solution given by leetcode for Approach 2: 'Greedy Way (Without Stack)'.
    Both the time and space complexity of this solution is O(n) in Python, however, the
    C++ implementation of this approach has space complexity of O(1) since it would
    require no additional data structures besides the string, since strings in C++ are
    mutable, while they are not in Python and Java. 
    """
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_points = 0
        s = list(s)

        if x > y:
            # Remove "ab" first (higher points), then "ba"
            total_points += self.remove_substring(s, "ab", x)
            total_points += self.remove_substring(s, "ba", y)
        else:
            # Remove "ba" first (higher or equal points), then "ab"
            total_points += self.remove_substring(s, "ba", y)
            total_points += self.remove_substring(s, "ab", x)

        return total_points

    def remove_substring(
        self, input_string, target_substring, points_per_removal
    ):
        total_points = 0
        write_index = 0

        # Iterate through the string
        for read_index in range(0, len(input_string)):
            # Add the current character
            input_string[write_index] = input_string[read_index]
            write_index += 1

            # Check if we've written at least two characters and
            # they match the target substring
            if (
                write_index > 1
                and input_string[write_index - 2] == target_substring[0]
                and input_string[write_index - 1] == target_substring[1]
            ):
                write_index -= 2
                total_points += points_per_removal

        # Trim the list to remove any leftover characters
        del input_string[write_index:]

        return total_points


class Solution:
    """
    Variant 5:
    My reproduction of Approach 3: 'Greedy Way (Counting)' given by leetcode to solve
    this problem. The time complexity of this is O(n) but the space complexity is O(1), 
    since we don't need to define a new string or list for this particular implementation. 
    """
    def maximumGain(self, s: str, x: int, y: int) -> int:
        num_points = 0
        aCount = 0
        bCount = 0
        if y > x:
            y_new_val = x
            x = y
            y = y_new_val
            s = s[::-1]
        for char in s:
            if char == 'a':
                aCount += 1
            elif char == 'b':
                if aCount > 0:
                    num_points += x
                    aCount -= 1
                else:
                    bCount += 1
            else:
                num_points += min(aCount, bCount)*y
                aCount = 0
                bCount = 0
                
        num_points += min(aCount, bCount)*y
        return num_points


class Solution:
    """
    Variant 6:
    The official implementation of  Approach 3: 'Greedy Way (Counting)' given by leetcode 
    to solve this problem. The time complexity of this is O(n) but the space complexity is 
    O(1), since we don't need to define a new string or list for this particular 
    implementation. 
    """
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Ensure "ab" always has higher points than "ba"
        if x < y:
            # Reverse the string to maintain logic
            s = s[::-1]
            # Swap points
            x, y = y, x

        a_count, b_count, total_points = 0, 0, 0

        for i in range(len(s)):
            if s[i] == "a":
                a_count += 1
            elif s[i] == "b":
                if a_count > 0:
                    # Can form "ab", remove it and add points
                    a_count -= 1
                    total_points += x
                else:
                    # Can't form "ab", keep 'b' for potential future "ba"
                    b_count += 1
            else:
                # Non 'a' or 'b' character encountered
                # Calculate points for any remaining "ba" pairs
                total_points += min(b_count, a_count) * y
                # Reset counters for next segment
                a_count = b_count = 0

        # Calculate points for any remaining "ba" pairs at the end
        total_points += min(b_count, a_count) * y

        return total_points



