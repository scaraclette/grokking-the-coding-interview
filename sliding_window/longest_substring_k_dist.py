"""
Given a string, find the length of the longest substring in it with no more 
than K distinct characters.
You can assume that K is less than or equal to the length of the given string.
"""

def longest_substring_with_k_distinct(str1, k):
    # max length of dictionary should be k
    letter_dict = {}
    max_substring = float('-inf')

    start = 0
    for end in range(len(str1)):
        if str1[end] not in letter_dict:
            letter_dict[str1[end]] = 1
        else:
            letter_dict[str1[end]] += 1

        if len(letter_dict) <= k:
            max_substring = max(max_substring, end - start + 1)
        else:
            # len(dict) is larger than k
            while start <= end or len(letter_dict) > k:
                letter_to_remove = str1[start]

                letter_dict[letter_to_remove] -= 1
                if letter_dict[letter_to_remove] == 0:
                    del letter_dict[letter_to_remove]
                
                start += 1

    return max_substring

def solution_longest_substring_with_k_distinct(str1, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # Shrink the sliding window
        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end-window_start + 1)
    
    return max_length



def main():
    print(longest_substring_with_k_distinct("aaraci", 2))
    print(longest_substring_with_k_distinct("aaraci", 1))
    print(longest_substring_with_k_distinct("cbbebi", 3))

main()