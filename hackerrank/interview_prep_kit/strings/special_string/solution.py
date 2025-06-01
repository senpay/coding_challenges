# A string is said to be a special string if either of two conditions is met:
# - All of the characters are the same, e.g. aaa.
# - All characters except the middle one are the same, e.g. aadaa.

# A special substring is any substring of a string which meets one of those criteria.
# Given a string, determine how many special substrings can be formed from it.

# Example
# s = "mnonopoo"
# s contains the following 12 special substrings:
# {m, n, o, n, o, p, o, o, non, ono, opo, oo}

# Function Description
# Complete the substrCount function.
# substrCount has the following parameter(s):
# - int n: the length of string s
# - string s: a string

# Returns
# - int: the number of special substrings

# Input Format
# The first line contains an integer, n, the length of s.
# The second line contains the string s.

# Constraints
# 1 ≤ n ≤ 10^6
# Each character of the string is a lowercase English letter, ascii[a-z].



def is_special_string(s):
    """From the strings patterns it seems we can identify special string using following checks:
    
    1) any string consisting of only one character
    2) any string consisting of two characters, where 1 (and only one) instance of the character is in the middle of the string
        2.1) so, it is only odd-length string""" 
    characters = set(s)
    if len(characters) == 1:
        # Simplest case
        return True
    elif len(characters) > 2:
        # Too many characters for special string
        return False
    elif len(s) % 2 == 0:
        # even length, no middle character, so False
        return False
    else:
        middle_character_index = len(s)// 2
        # check if excluding middle characters will leave us with single character string
        return len(set(s[:middle_character_index] + s[middle_character_index + 1:])) == 1



# Complete the substrCount function below.
def substrCount(n, s):
    special_strings = 0

    if len(s) < 2:
        return len(s)

    left_index = 0
    right_index = 1

    # we will go through string and build substrings, as soon as we hit "not special" - we will stop
    while left_index < len(s):
        candidate_substring = s[left_index:right_index]
        if is_special_string(candidate_substring):
            special_strings += 1
            right_index += 1
            if right_index == len(s) + 1:
                left_index += 1
                right_index = left_index + 1
        else:
            possible_substring = candidate_substring + s[right_index:right_index + (right_index - left_index) - 1]
            if is_special_string(possible_substring):
                 special_strings += 1
            left_index += 1
            right_index = left_index + 1

    return special_strings

