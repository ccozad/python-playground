# Valid parens
# Check that a string balanced braces
# Problem constraints
# 1. The only contains the characters '(', ')', '{', '}', '[' and ']'
# 2. Open brackets must be closed by the same type of bracket
# 3. Open brackets must be closed in the correct order

# For this problem we will rely on the properties of a stack
# data structure. A stack is a last in first out data structure
# that makes it easy to keep track of the most recent item
# added to storage.
#
# Python has methods that allow an ordinary list to be accessed
# like a stack.

def is_valid_parens(s: str) -> bool:
    bracket_stack = []
    
    # We'll need to look up what brackets are considered opening brackets
    # and we need to know what correct closing bracket is.
    brackets = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    
    for letter in s:
        if letter in brackets:
            # The item is an opening bracket, we need to remember it
            # by adding it to the end of the list (i.e. the top of the stack)
            bracket_stack.append(letter)
        else:
            # Otherwise the item is a closing bracket
            # If the bracket stack is not empty we can check the
            # to see if we have the right opening bracket
            if len(bracket_stack) > 0:
                # pop() with no parameters returns the last item in the list
                last_bracket = bracket_stack.pop()
                # Fail if we don't have the correct closing bracket
                if brackets[last_bracket] != letter:
                    return False
            else:
                # We have a closing bracket with no opening bracket
                # Fail the check
                return False
    
    # Fail the validation if there are any orphaned brackets
    # Otherwise the validation passes
    return len(bracket_stack) == 0