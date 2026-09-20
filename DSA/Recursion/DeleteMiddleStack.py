# Delete Middle Element in Stack using Recursion
def deleteMiddle(stack, k):
    if len(stack) == 0:
        return
    
    if k == 1:
        stack.pop()
        return
    
    temp = stack.pop()
    deleteMiddle(stack, k - 1)
    stack.append(temp)


# Example usage
stack = [1, 2, 3, 4, 5]
k = (len(stack) // 2) + 1  # Middle element position

deleteMiddle(stack, k)
print(stack)  # Output: [1, 2, 4, 5]