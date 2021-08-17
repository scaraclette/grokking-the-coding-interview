def smallest_subsegment(arr):
    # To store left most occurrence of elements
    first_num_index = {}

    # To store counts of elements
    num_frequency = {}

    highest_num_frequency = 0

    smallest_string_length = 0
    starting_index = 0

    for i in range(len(arr)):
        current_num = arr[i]

        if current_num not in first_num_index:
            first_num_index[current_num] = i
            num_frequency[current_num] = 1
        else:
            # Increase frequency of elements
            num_frequency[current_num] += 1
        
        # Find maximum repeated element and
        # store its last occurence and first occurenc
        current_length = i - first_num_index[current_num] + 1
        if num_frequency[current_num] > highest_num_frequency:
            highest_num_frequency = num_frequency[current_num]
            smallest_string_length = current_length
            starting_index = first_num_index[current_num]
        elif (num_frequency[current_num] == highest_num_frequency and current_length < smallest_string_length):
            smallest_string_length = current_length
            starting_index = first_num_index[current_num]
    
    print(arr[starting_index: starting_index + smallest_string_length])



def main():
    # arr = [4, 1, 1, 2, 2, 1, 3, 3]
    # smallest_subsegment(arr)
    arr = [1,2,2,3,1,4,2]
    smallest_subsegment(arr)

main()