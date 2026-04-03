"""
273. Integer to English Words
Solved
Hard

Topics

Companies

Hint
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
"""

class Solution:
    """
    Variant 1: 
    My first successful submission to solve this problem without referencing any of the
    provided solutions! I think this is the first hard LC problem that I essentially
    solved on my own. My hopefully educated guess is that the time complexity is (O(n))
    where n is the number of digits in 'num', since the number of iterations of the while
    loop in numberToWords depends on the number of digits in num. I am guessing that the
    space complexity is either O(n) or O(1) but I am not sure. This code was unfortunately
    too long for LC to be able to analyze :( However, accoring to real efficiency metrics,
    this solution beats almost 100% of accepted answers in terms of RT efficiency. This 
    solution beats ~28% of accepted answers in terms of memory efficiency. I am curious to
    see how the provided solutions perform...
    """
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        num = str(num)
        ret_str = ''
        teen_names_lookup = {
            '10' : 'Ten',
            '11' : 'Eleven',
            '12' : 'Twelve',
            '13' : 'Thirteen',
            '14' : 'Fourteen',
            '15' : 'Fifteen',
            '16' : 'Sixteen',
            '17' : 'Seventeen',
            '18' : 'Eighteen',
            '19' : 'Nineteen'
        }

        ones_names_lookup = {
            '1' : 'One',
            '2' : 'Two',
            '3' : 'Three',
            '4' : 'Four',
            '5' : 'Five',
            '6' : 'Six',
            '7' : 'Seven',
            '8' : 'Eight',
            '9' : 'Nine'
        }

        tens_place_lookup = {
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '6': 'Sixty',
            '7': 'Seventy',
            '8': 'Eighty',
            '9': 'Ninety'
        }
        def return_num_ones(ret_str, dig):
            ret_str = ret_str + ' ' + ones_names_lookup[dig]
            return ret_str

        def return_num_tens(ret_str, digs):
            print(digs)
            print(ret_str)
            if digs[0] != '1':
                ret_str = ret_str + ' ' + tens_place_lookup[digs[0]]
            else:
                print(teen_names_lookup)
                ret_str = ret_str + ' ' + teen_names_lookup[digs]
            return ret_str
            
        def return_num_hundreds(ret_str, dig):
            ret_str = ret_str + ' ' + ones_names_lookup[dig] + ' ' + 'Hundred'
            return ret_str

        places = ['', ' Thousand', ' Million', ' Billion']
        place_index = 0
        rem_nums = num
        ret_str_list = []
        while place_index < 4 and len(rem_nums) > 0:
            print(rem_nums)
            if len(rem_nums) > 3:
                chunk = rem_nums[-3:]
                rem_nums = rem_nums[:-3]
            else:
                chunk = rem_nums
                rem_nums = ''
            ret_str = ''
            if len(chunk) == 3 and chunk[0] != '0':
                ret_str = return_num_hundreds(ret_str, chunk[0])
                print(ret_str)
            if len(chunk) >= 2:
                if chunk[-2] != '0':
                    #print(chunk[-2:])
                    ret_str = return_num_tens(ret_str, chunk[-2:])
                    #print('ret_str')
                    #print(ret_str)
            if chunk[-1] != '0':
                if len(chunk) >= 2:
                    if chunk[-2] != '1':
                        ret_str = return_num_ones(ret_str, chunk[-1])
                        print(ret_str)
                else:
                    ret_str = return_num_ones(ret_str, chunk[-1])
                    print(ret_str)
            if ret_str != '':
                final_ret_str = ret_str + places[place_index]
                print('final return str')
                print(final_ret_str)
                ret_str_list.append(final_ret_str[1:])
            place_index += 1
            
        ret_str_list.reverse()

        if len(ret_str_list) > 1:
            return ' '.join(ret_str_list)
        else:
            return ret_str_list[0] 


class Solution:
    """
    Variant 2:
    This is the official solution for this problem provided by LC for 'Approach 1: Recursive 
    Approach'. I have to admit this is a quite elegant and somewhat intuitive approach.
    Although this solution shows slightly higher efficiency compared to Variant 1, beating
    almost 100% of accepted answers in RT efficiency as well but also ~50% of accepted answers in
    memory efficiency. LC's analysis tool says this algorithm has O(logN) time efficiency which
    kinda makes sense if you think of the number of digits or places (powers of ten) as scaling
    with N as logN. So I think the same is true for Variant 1 (it having O(lognums) TC). The AT
    says that the space efficiency is also O(logn), and so is Variant 1's probably. And the
    Editorial section even goes as far to say that the time complexity is technically O(log{base10}N)
    and the same is true for the space complexity. Excellent!
    """
    # Arrays to store words for numbers less than 10, 20, and 100
    below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    below_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    # Main function to convert a number to English words
    def numberToWords(self, num: int) -> str:
        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"
        # Call the helper function to start the conversion
        return self._convert_to_words(num)

    # Recursive function to convert numbers to words
    # Handles numbers based on their ranges: <10, <20, <100, <1000, <1000000, <1000000000, and >=1000000000
    def _convert_to_words(self, num: int) -> str:
        if num < 10:
            return self.below_ten[num]
        if num < 20:
            return self.below_twenty[num - 10]
        if num < 100:
            return self.below_hundred[num // 10] + (" " + self._convert_to_words(num % 10) if num % 10 != 0 else "")
        if num < 1000:
            return self._convert_to_words(num // 100) + " Hundred" + (" " + self._convert_to_words(num % 100) if num % 100 != 0 else "")
        if num < 1000000:
            return self._convert_to_words(num // 1000) + " Thousand" + (" " + self._convert_to_words(num % 1000) if num % 1000 != 0 else "")
        if num < 1000000000:
            return self._convert_to_words(num // 1000000) + " Million" + (" " + self._convert_to_words(num % 1000000) if num % 1000000 != 0 else "")
        return self._convert_to_words(num // 1000000000) + " Billion" + (" " + self._convert_to_words(num % 1000000000) if num % 1000000000 != 0 else "")


class Solution:
    """
    Variant 3:
    Official solution provided by LC for 'Approach 2: Iterative Approach'. Supposedly its
    space complexity is O(1). This actually seems closer to what I did than Variant 2.
    """
    def numberToWords(self, num: int) -> str:
        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"

        # Arrays to store words for single digits, tens, and thousands
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        # StringBuilder to accumulate the result
        result = ""
        group_index = 0

        # Process the number in chunks of 1000
        while num > 0:
            # Process the last three digits
            if num % 1000 != 0:
                group_result = ""
                part = num % 1000

                # Handle hundreds
                if part >= 100:
                    group_result += ones[part // 100] + " Hundred "
                    part %= 100

                # Handle tens and units
                if part >= 20:
                    group_result += tens[part // 10] + " "
                    part %= 10

                # Handle units
                if part > 0:
                    group_result += ones[part] + " "

                # Append the scale (thousand, million, billion) for the current group
                group_result += thousands[group_index] + " "
                # Insert the group result at the beginning of the final result
                result = group_result + result
            # Move to the next chunk of 1000
            num //= 1000
            group_index += 1

        return result.strip()