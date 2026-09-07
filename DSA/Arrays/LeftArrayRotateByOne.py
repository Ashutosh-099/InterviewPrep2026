# Rotate Array by One Position to the Left

def left_rotate_by_one(arr):
    if len(arr) < 2:
        return
    
    value = arr[0]

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]

    arr[i] = value

    return

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    left_rotate_by_one(arr)
    print("Array after left rotation by one position:", arr)