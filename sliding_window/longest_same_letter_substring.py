"""
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more 
than ‘k’ letters with any letter, 
find the length of the longest substring having the same letters after replacement.
"""

def white_length_of_longest_substring(str, k):
    window_start = 0
    max_length = 0

    # Max_count variable to keep track of the longest set of characters
    max_count = 0
    counter = {}

    for window_end in range(len(str)):
        end_char = str[window_end]
        if end_char not in counter:
            counter[end_char] = 1
        else:
            counter[end_char] += 1

        current_char_count = counter[end_char]
        max_count = max(max_count, current_char_count)

        while (window_end - window_start - max_count + 1 > k):
            start_char = str[window_start]
            counter[start_char] -= 1
            if counter[start_char] == 0:
                del counter[start_char]
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
        
    return max_length

def solution_length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])

        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


if __name__=="__main__":
    print(white_length_of_longest_substring("bbccabx", 3))