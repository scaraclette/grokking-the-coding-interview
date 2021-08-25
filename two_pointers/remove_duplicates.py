def remove_duplicates(arr):
    index_next_non_duplicate = 1

    i = 1
    while (i < len(arr)):
        if arr[index_next_non_duplicate - 1] != arr[i]:
            arr[index_next_non_duplicate] = arr[i]
            index_next_non_duplicate += 1
        i += 1

    return index_next_non_duplicate

def remove_duplicates_2(arr):
    slow = 0
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1

def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))

main()