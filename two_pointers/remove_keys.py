def remove_key(arr, k):
    non_key_index = 0
    for i in range(len(arr)):
        if arr[i] != k:
            arr[non_key_index] = arr[i]
            non_key_index += 1

    return non_key_index 