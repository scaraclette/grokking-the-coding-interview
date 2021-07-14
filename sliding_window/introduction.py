def find_averages_of_subarrays(k, arr):
    result = []

    for i in range(len(arr) - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]

        result.append(current_sum / k)

    return result

# Optimized find averages
def optimized_find_averages(k, arr):
    result = []
    _sum = 0

    for i in range(len(arr)):
        _sum += arr[i]

        # Case when is within limit
        if (i <= k - 1):
            result.append(_sum / k)
            _sum -= arr[i-k]
            

    return result

# Grokking solution
def solution_find_averages(k, arr):
    result = []
    windowSum, windowStart = 0.0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= k - 1:
            result.append(windowSum / k)
            windowSum -= arr[windowStart]
            windowStart += 1
    
    return result

def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))

main()