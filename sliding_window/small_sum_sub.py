"""
Given an array of positive numbers and a positive number ‘S,’ 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0 if no such subarray exists.
"""

def smallest_subarray_with_given_sum(s, arr):
    start = 0
    current_sum = 0
    min_index = float('inf')

    for end in range(len(arr)):
        # Increment current sum
        current_sum += arr[end]

        # Check if bigger than equals k
        if current_sum >= s:
            min_index = min(min_index, (end - start) + 1)

        while start <= end:
            if current_sum - arr[start] >= s:
                current_sum -= arr[start]
                start += 1
                new_index = end - start + 1
                min_index = min(min_index, new_index)
            else:
                break
    
    return min_index

def solution_smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length = float('inf')
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        # Shrink the window as small as possible until the 'window_sum' is smaller than s
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    if min_length == float('inf'):
        return 0
    
    return min_length



def main():
    print(smallest_subarray_with_given_sum(3, [2, 1, 4]))
    print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))


main()