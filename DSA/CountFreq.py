# Count frequency of elements in an array

def count_frequency(arr):
    freq_dict = {}

    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    return freq_dict

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    frequency = count_frequency(arr)
    # Convert the frequency dictionary to array of tuples for better readability
    frequency_array = [[key, value] for key, value in frequency.items()]
    print(frequency)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}
    print(frequency_array)  # Output: [[1, 1], [2, 2], [3, 3], [4, 4]]