def pair_with_targetsum(arr, target_sum):
  left, right = 0, len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:
      return [left, right]

    if target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum
  return [-1, -1]

def pair_with_targetsum_dict(arr, target_sum):
    pair_index = {}

    for i, num in enumerate(arr):
        if num in pair_index:
            return [pair_index[num], i]
        target = target_sum - num
        pair_index[target] = i
        print(pair_index)
    
    return [-1, -1]

def pair_with_targetsum_solution(arr, target_sum):
    nums = {}
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[num] = i
        print(nums)
    return [-1, -1]

def main():
  print(pair_with_targetsum_dict([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum_dict([2, 5, 9, 11], 11))
  print("----------------")
  print(pair_with_targetsum_solution([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum_solution([2, 5, 9, 11], 11))


main()