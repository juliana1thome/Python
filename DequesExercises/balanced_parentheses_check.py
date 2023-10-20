# Given a string of opening and closing parentheses, check whether it's balanced
# We have 2 types of parentheses: round brackets (), square brackets [], curly brackets {}
# Assume that the string doesn't contain any other character than these, no spaces words or numbers
# Examples balanced parentheses: '{()}'
# Example of not balanced parentheses: '([)]'

# This exercise is the same as the one on stack folder, but it is using deque (but the operations are the same as stacks)

from Deque import Deque

def balance_check(string):

    # First check before processing any logic is to check if the are pairs
    if len(string)%2 != 0:
        return False

    # Create an empty deque to keep track of opening parentheses
    deque = Deque()

    # Define a mapping of open and closed parentheses
    parentheses_map = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    # Iterate char by char in the string
    for char in string:
        # If it's an opening parenthesis, push it onto the deque
        if char in '({[':
            deque.addFront(char)

        # If it's a closing parenthesis
        elif char in ')}]':
            # If the stack is empty, it's not balanced
            if deque.size == 0:
                return False

            # Check if the opening that is mapped matches the top of the deque
            if deque.items[-1] == parentheses_map[char]:
                # Remove the matching opening parenthesis
                deque.removeFront()

            else:
                # Mismatched parentheses
                return False

    # After processing the entire string, the stack should be empty for balanced parentheses
    return len(deque.items) == 0

# Test the function
assert (balance_check('[{]')) == False
assert (balance_check('[{}]')) == True
assert (balance_check('[{]}')) == False
