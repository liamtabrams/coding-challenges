"""
17. Letter Combinations of a Phone Number
Solved
Medium

Topics

Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

import random

class Solution:
    """
    Variant 1:
    My first successful attempt at solving this problem. My educated guess is that the
    run time complexity of this solution is O(N^4) (where N is the length of digits) in
    the worst case and that the space complexity of this solution is O(N^4). Let's see
    what leetcode says about my solution. It analyzed the run time complexity AND the
    space complexity of this solution to be O(2^N * N), which, when N = 4 gives O(16 * N)
    which evaluates to O(N^3) as the worst case. This is only true because of the 
    constraint 0 <= digits.length <= 4, and the answer I gave is not generally correct.
    So saying that this solution has exponential complexity is more accurate than saying
    it has quartic complexity. Also, this particular solution only beats ~25% and ~15% of
    accepted answers in terms of run time and memory efficiency, respectively. How can we
    improve on this to make it more efficient? To be honest I'm not sure. I think we just
    need a better approach, rather than trying to optimize this one. 
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        phone_buttons = {'2': ['a', 'b', 'c'],
                         '3': ['d', 'e', 'f'],
                         '4': ['g', 'h', 'i'],
                         '5': ['j', 'k', 'l'],
                         '6': ['m', 'n', 'o'],
                         '7': ['p', 'q', 'r', 's'],
                         '8': ['t', 'u', 'v'],
                         '9': ['w', 'x', 'y', 'z']
        }
        digits = list(digits)
        possible_combos = []
        num_expected = len(phone_buttons[digits[0]])
        for i in range(1, len(digits)):
            num_expected = num_expected*len(phone_buttons[digits[i]])
        while len(possible_combos) < num_expected:
            combo = ''
            for i in range(len(digits)):
                combo += random.choice(phone_buttons[digits[i]])
            if combo not in possible_combos:
                possible_combos.append(combo)
        
        return possible_combos


class Solution:
    """
    Variant 2:
    My successful reenactment of the single solution 'Approach 1: Backtracking' provided
    by Leetcode for this problem. My educated guess is that this solution has run time
    and space complexity of O(4^N) in the worst case, where N is the length of 'digits', 
    since there are up to 4^N different paths/combinations we have to generate and store.
    However, according to the Editorial section, the run time complexity is actually
    O(N * 4^N) and the space complexity is actually O(N). 
    
    Someone in the comments helped clarify the extra factor of N for the run time complexity, 
    explaining "So that a total of (4^N * N) characters that whatever code you write will 
    have to output/generate/copy/print, one way or another, character by character. So the 
    best you can do is (4^N * N) time."

    For the space complexity, the editorial section explains
    "Not counting space used for the output, the extra space we use relative to input 
    size is the space occupied by the recursion call stack. It will only go as deep as 
    the number of digits in the input since whenever we reach that depth, we backtrack.
    As the hash map does not grow as the inputs grows, it occupies O(1) space."

    When I have Leetcode analyze the submitted answer's complexity, it reports O(3^N * 4^M)
    for both the runtime and memory complexity. Honestly, I am not sure if N and M represent
    the number of digits representing 3 or 4 different letters respectively in the input,
    or something else. When I ask ChatGPT to clarify, it confirms my assumption. So even
    though my initial thoughts on the runtime and space complexity differed from what the
    Editorial section stated to be true, Leetcode's analysis of my submitted solution agrees
    with those initial thoughts. This might be due to language-specific differences in how
    the algorithm is implemented, and maybe the Editorial's explanation of the complexity
    of this approach is not accurate for Python.

    Anyway, this particular solutions beats ~60% and ~20% of accepted answers in terms of
    runtime and memory efficiency, respectively. I will compare these performance metrics
    to the official solution for this approach provided by Leetcode.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        phone_buttons = {'2': ['a', 'b', 'c'],
                         '3': ['d', 'e', 'f'],
                         '4': ['g', 'h', 'i'],
                         '5': ['j', 'k', 'l'],
                         '6': ['m', 'n', 'o'],
                         '7': ['p', 'q', 'r', 's'],
                         '8': ['t', 'u', 'v'],
                         '9': ['w', 'x', 'y', 'z']
        }
        digits = list(digits)
        possible_combos = []
        def backtrack(index, path):
            if len(path) == len(digits):
                possible_combos.append(''.join(path))
                return

            possible_letters = phone_buttons[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()


        backtrack(0, [])
        return possible_combos


class Solution:
    """
    Variant 3:
    The official single solution given by Leetcode for this problem, 'Approach 1: 
    Backtracking'. I already gave a synopsis in the description of Variant 2 for the 
    Editorial's explanation of runtime and space complexity for this approach. There
    shouldn't be any difference in terms of performance between this implementation
    and mine, but I will still compare the average performance metrics of this one to
    Variant 2's. Indeed, they look the same.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations