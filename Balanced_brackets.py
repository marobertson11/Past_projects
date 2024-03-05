#This program will state if a given bracket/parenthesis statement is balanced,
# meaning that for each beginning parenthesis or bracket has a closing one 
# in the right order

#Example: ([]) is balanced
#Example: ([) is  not balanced
#Example: ([)] while it does have the correct amount of openings and closing, 
#  it is not in the right order

def areBracketsBalanced(expr):
    stack = [] 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
            # Push the element in the stack
            stack.append(char)
        else:
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 
# Driver Code
if __name__ == "__main__":
    expr = input("Please enter the bracket statement: ")
 
    # Function call
    
    if areBracketsBalanced(expr):
        print("'" + expr + "' is balanced")
    else:
        print("'" + expr + "' is not balanced")