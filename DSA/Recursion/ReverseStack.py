# Reverse a stack using recursion
def insertAtBottom(stack, value):
    if len(stack) == 0:
        stack.append(value)
        return stack
    
    top = stack.pop()
    stack = insertAtBottom(stack, value)
    stack.append(top)
    return stack

def reverse(stack):
    if len(stack) <= 1:
        return stack
    
    pivot = stack.pop()
    reversedStack = reverse(stack)
    # Insert pivot at the bottom of reversedStack
    return insertAtBottom(reversedStack, pivot)

# Example usage
stack = [5, 2, 9, 1, 5, 6]
reversed_stack = reverse(stack)
print(reversed_stack)