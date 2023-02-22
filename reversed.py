def reverse_python_statement(statement):
    """
    Reverses the evaluation of a Python statement.
    """
    # Define a stack to hold the parts of the statement
    stack = []
    
    # Split the statement into tokens
    tokens = statement.split()
    
    # Process each token
    for token in tokens:
        # Check if the token is a negation
        if token == 'not':
            # Negate the previous token and push it onto the stack
            prev_token = stack.pop()
            if prev_token.startswith('(') and prev_token.endswith(')'):
                prev_token = reverse_python_statement(prev_token[1:-1])
            stack.append(f"not {prev_token}")
        # Check if the token is a comparison operator
        elif token in ['==', '!=', '<', '>', '<=', '>=']:
            # Pop the previous two tokens and create a new expression with the comparison operator reversed
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.append(f"{left_operand} {reverse_operator(token)} {right_operand}")
        # Otherwise, push the token onto the stack
        else:
            stack.append(token)
    
    # Combine the tokens on the stack into a single string
    return ' '.join(stack)

def reverse_operator(operator):
    """
    Returns the reverse of a comparison operator.
    """
    if operator == '==':
        return '!='
    elif operator == '!=':
        return '=='
    elif operator == '<':
        return '>='
    elif operator == '>':
        return '<='
    elif operator == '<=':
        return '>'
    elif operator == '>=':
        return '<'
