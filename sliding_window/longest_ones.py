"""
Problem Statement #
Given an array containing 0s and 1s, 
if you are allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.
"""

def length_of_longest_substring(arr, k):
    start = 0
    count_arr = [0, 0]
    count_ones = 0
    longest_ones = 0

    for end in range(len(arr)):
        end_num = arr[end]
        count_arr[end_num] += 1

        # See if ones are longer
        count_ones = max(count_ones, count_arr[1])

        while (end - start - count_ones + 1 > k):
            start_num = arr[start]
            count_arr[start_num] -= 1
            start += 1
        
        longest_ones = max(longest_ones, end - start + 1)
    
    return longest_ones



if __name__=="__main__":
    print(length_of_longest_substring([1, 0, 0, 1], 1))