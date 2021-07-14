"""
Problem Statement #
Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.
Goal: O(n) time, O(1) space
"""

def brute_max_sub_array_of_size_k(k, arr):
    max_sum = float('-inf')

    for i in range(len(arr) - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]
        
        max_sum = max(current_sum, max_sum)

    return max_sum

def max_sub_array_of_size_k(k, arr):
    max_sum = float('-inf')

    current_sum, start_window = 0, 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if i >= k - 1:
            max_sum = max(max_sum, current_sum)

            current_sum -= arr[start_window]
            start_window += 1
    
    return max_sum

def main():
    max_sum_1 = max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
    max_sum_2 = brute_max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
    print(max_sum_2)

main()