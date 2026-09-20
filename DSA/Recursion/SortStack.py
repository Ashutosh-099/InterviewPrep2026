# Sort Stack function using recursion
def insertIntoStack(stack, pivot):
    if len(stack) == 0 or stack[-1] <= pivot:
        stack.append(pivot)
        return stack
    
    value = stack.pop()
    sortedStack = insertIntoStack(stack, pivot)
    sortedStack.append(value)
    return sortedStack

def sortStack(stack):
    if len(stack) <= 1:
        return stack
    
    pivot = stack.pop()
    sortedStack = sortStack(stack)

    # Now add pivot into sortedStack
    return insertIntoStack(sortedStack, pivot)

# Example usage
stack = [5, 2, 9, 1, 5, 6]
sorted_stack = sortStack(stack)
print(sorted_stack)