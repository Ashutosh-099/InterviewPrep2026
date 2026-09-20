# Sort an array using recursion
def insertIntoArray(arr, pivot):
    if len(arr) == 0 or arr[-1] <= pivot:
        arr.append(pivot)
        return arr
    
    value = arr.pop()
    arr = insertIntoArray(arr, pivot)
    arr.append(value)
    return arr

def sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    sortArray = sort(arr[:-1])

    # Now add pivot into SortArray
    return insertIntoArray(sortArray, pivot)    

# Example usage
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = sort(arr)
print(sorted_arr)