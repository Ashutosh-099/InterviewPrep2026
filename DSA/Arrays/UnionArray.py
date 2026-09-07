# Union of two sorted array, The elements in the union must be in ascending order. The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.
def unionArray(nums1, nums2):
    i = 0
    j = 0

    result = []
    result.append(min(nums1[0], nums2[0]))

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if nums1[i] != result[-1]:
                result.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if nums2[j] != result[-1]:
                result.append(nums2[j])
            j += 1
        elif nums1[i] == nums2[j]:
            if nums1[i] != result[-1]:
                result.append(nums1[i])
            i += 1
            j += 1

    while i < len(nums1):
        if nums1[i] != result[-1]:
            result.append(nums1[i])
        i += 1

    while j < len(nums2):
        if nums2[j] != result[-1]:
            result.append(nums2[j])
        j += 1

    return result


nums1 = [3, 4, 4, 4]
nums2 = [6, 7, 7]

print("Union of two sorted arrays:", unionArray(nums1, nums2))