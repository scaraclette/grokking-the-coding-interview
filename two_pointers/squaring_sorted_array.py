def make_squares(arr):
    result_arr = [0 for x in range(len(arr))]

    highest_index = len(arr) - 1
    left = 0
    right = len(arr) - 1
    while left <= right:
        left_squared = pow(arr[left], 2)
        right_squared = pow(arr[right], 2)
        print("left_squared:", left_squared, ", right_squared:", right_squared)

        if left_squared > right_squared:
            result_arr[highest_index] = left_squared
            left += 1
        else:
            result_arr[highest_index] = right_squared
            right -= 1
        print(result_arr)
        highest_index -= 1
    
    return result_arr

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()