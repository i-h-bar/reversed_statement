import ast

def reverse_python_statement(statement):
    """
    Reverses the evaluation of a Python statement.
    """
    # Parse the statement into an abstract syntax tree
    tree = ast.parse(statement)
    
    # Traverse the tree and modify the nodes
    def traverse(node):
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            # If the node is a negation, remove the negation and process the operand
            operand = traverse(node.operand)
            if isinstance(operand, ast.UnaryOp) and isinstance(operand.op, ast.Not):
                # If the operand is also a negation, remove the double negation
                return operand.operand
            else:
                return ast.UnaryOp(op=ast.Not(), operand=operand)
        elif isinstance(node, ast.Compare):
            # If the node is a comparison, reverse the operator and swap the left and right operands
            left_operand = ast.unparse(node.left).strip()
            right_operand = ast.unparse(node.comparators[0]).strip()
            operator = reverse_operator(ast.unparse(node.ops[0]).strip())
            return ast.parse(f"{right_operand} {operator} {left_operand}").body[0].value
        elif isinstance(node, ast.BoolOp) and isinstance(node.op, ast.And):
            # If the node is a conjunction, recursively process the left and right operands and swap them
            left_operand = traverse(node.values[0])
            right_operand = traverse(node.values[1])
            return ast.BoolOp(op=ast.And(), values=[right_operand, left_operand])
        else:
            # Otherwise, return the original node
            return node
    
    # Traverse the tree and generate the modified statement
    modified_tree = traverse(tree)
    modified_statement = ast.unparse(modified_tree).strip()
    
    return modified_statement

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
