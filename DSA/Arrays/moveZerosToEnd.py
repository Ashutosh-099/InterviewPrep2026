# Move all the zeros to the end of the array while maintaining the relative order of the non-zero elements.

def move_zeros_to_end(arr):
    if len(arr) < 2:
        return
    
    i = 0

    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1

    while i < len(arr):
        arr[i] = 0
        i += 1

if __name__ == "__main__":
    arr = [0, 20, 0, -20, 0, 20]
    print("Original array:", arr)
    move_zeros_to_end(arr)
    print("Array after moving zeros to the end:", arr)